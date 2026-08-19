# SPDX-License-Identifier: GPL-3.0-or-later
"""File identity and guarded atomic UTF-8 persistence for Schedulae."""
from __future__ import annotations

from dataclasses import dataclass
import errno
import hashlib
import os
import stat
import tempfile
from typing import Any


@dataclass(frozen=True)
class FileToken:
    exists: bool
    mtime_ns: int = 0
    size: int = 0
    digest: str = ""


class FileConflictError(Exception):
    """Raised when the destination changes during one guarded write."""

    def __init__(self, token: FileToken) -> None:
        super().__init__("file changed before atomic replace")
        self.token = token


def _validate_path(path: str) -> str:
    if not isinstance(path, str) or not path:
        raise ValueError("path is required")
    return path


def _regular_lstat(path: str) -> os.stat_result | None:
    """Return lstat for an existing regular non-symlink path, or None if absent."""
    try:
        info = os.lstat(path)
    except FileNotFoundError:
        return None
    if stat.S_ISLNK(info.st_mode):
        raise OSError(errno.ELOOP, "destination must not be a symbolic link", path)
    if not stat.S_ISREG(info.st_mode):
        raise OSError(errno.EINVAL, "destination must be a regular file", path)
    return info


def file_token(path: str) -> FileToken:
    if not isinstance(path, str) or not path:
        return FileToken(False)
    try:
        info = os.stat(path)
    except FileNotFoundError:
        return FileToken(False)
    if not stat.S_ISREG(info.st_mode):
        raise OSError(errno.EINVAL, "path is not a regular file", path)
    with open(path, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    return FileToken(True, info.st_mtime_ns, info.st_size, digest)


def _same_temp_identity(path: str, expected: tuple[int, int]) -> bool:
    try:
        info = os.lstat(path)
    except FileNotFoundError:
        return False
    return stat.S_ISREG(info.st_mode) and (info.st_dev, info.st_ino) == expected


def _cleanup_owned_temp(path: str, expected: tuple[int, int]) -> None:
    try:
        if _same_temp_identity(path, expected):
            os.unlink(path)
    except OSError:
        pass


def _fsync_directory(directory: str) -> None:
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    try:
        fd = os.open(directory, flags)
    except OSError:
        return
    try:
        try:
            os.fsync(fd)
        except OSError:
            # Directory fsync is not supported uniformly across filesystems.
            pass
    finally:
        os.close(fd)


def atomic_write_utf8(
    path: str,
    text: Any,
    *,
    expected_token: FileToken | None = None,
) -> FileToken:
    """Atomically replace one regular file using an operation-owned same-dir temp.

    ``expected_token`` narrows the stale-write boundary: it is checked after the
    temporary file has been fully written/fsynced and immediately before publish.
    """
    path = _validate_path(path)
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    directory = os.path.dirname(path) or os.curdir
    os.makedirs(directory, exist_ok=True)
    current_info = _regular_lstat(path)
    mode = stat.S_IMODE(current_info.st_mode) if current_info is not None else 0o600

    prefix = f".{os.path.basename(path)}.schedulae-"
    fd, tmp_path = tempfile.mkstemp(prefix=prefix, suffix=".tmp", dir=directory, text=False)
    tmp_info = os.fstat(fd)
    owned = (tmp_info.st_dev, tmp_info.st_ino)
    try:
        os.fchmod(fd, mode)
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            fd = -1
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())

        if not _same_temp_identity(tmp_path, owned):
            raise OSError(errno.EIO, "temporary file identity changed during save", tmp_path)

        # Reject a destination that was swapped to a symlink/non-regular object,
        # then perform the stale-token check as the final read before publish.
        _regular_lstat(path)
        if expected_token is not None:
            current = file_token(path)
            if current != expected_token:
                raise FileConflictError(current)

        os.replace(tmp_path, path)
        _fsync_directory(directory)
        return file_token(path)
    except BaseException:
        if fd >= 0:
            try:
                os.close(fd)
            except OSError:
                pass
        _cleanup_owned_temp(tmp_path, owned)
        raise

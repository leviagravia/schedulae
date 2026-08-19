# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import os
from pathlib import Path
import socket
import stat
import tempfile
import unittest
from unittest import mock

from schedulae.reference_store import MarkdownReferenceStore
from schedulae.references import ReferenceRecord
from schedulae.research_file import FileToken, atomic_write_utf8, file_token


class B01FileSafetyTests(unittest.TestCase):
    def record(self, title="Title"):
        return ReferenceRecord(key="key2026", title=title)

    def test_explicit_absolute_library_path_works_and_is_normalized_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "nested", "references.md")
            store = MarkdownReferenceStore(path)
            self.assertTrue(os.path.isabs(store.path))
            self.assertEqual(store.path, os.path.realpath(path))
            result = store.save((self.record(),), store.load().token)
            self.assertTrue(result.saved, result.message)

    def test_selected_symlink_preserves_link_and_updates_frozen_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "target.md"
            link = Path(tmp) / "library.md"
            initial = MarkdownReferenceStore(str(target))
            self.assertTrue(initial.save((self.record("Before"),), initial.load().token).saved)
            link.symlink_to(target)
            store = MarkdownReferenceStore(str(link))
            self.assertEqual(store.selected_path, str(link))
            self.assertEqual(store.path, str(target))
            snap = store.load()
            saved = store.save((self.record("After"),), snap.token)
            self.assertTrue(saved.saved, saved.message)
            self.assertTrue(link.is_symlink())
            self.assertEqual(store.load().records[0].title, "After")

    def test_legacy_fixed_tmp_symlink_cannot_touch_victim(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "references.md"
            victim = Path(tmp) / "victim.txt"
            legacy_tmp = Path(str(path) + ".tmp")
            victim.write_text("DO_NOT_TOUCH", encoding="utf-8")
            legacy_tmp.symlink_to(victim)
            atomic_write_utf8(str(path), "SAFE DATA\n")
            self.assertEqual(victim.read_text(encoding="utf-8"), "DO_NOT_TOUCH")
            self.assertTrue(legacy_tmp.is_symlink())
            self.assertEqual(path.read_text(encoding="utf-8"), "SAFE DATA\n")

    def test_unique_temp_is_same_directory_and_operation_owned(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "references.md"
            real_mkstemp = tempfile.mkstemp
            calls = []
            def wrapped(*args, **kwargs):
                result = real_mkstemp(*args, **kwargs)
                calls.append((args, kwargs, result[1]))
                return result
            with mock.patch("schedulae.research_file.tempfile.mkstemp", side_effect=wrapped):
                atomic_write_utf8(str(path), "x\n")
            self.assertEqual(len(calls), 1)
            self.assertEqual(Path(calls[0][2]).parent, Path(tmp))
            self.assertNotEqual(calls[0][2], str(path) + ".tmp")
            self.assertFalse(Path(calls[0][2]).exists())

    def test_existing_mode_is_preserved_and_new_file_is_private(self):
        with tempfile.TemporaryDirectory() as tmp:
            existing = Path(tmp) / "existing.md"
            existing.write_text("old", encoding="utf-8")
            os.chmod(existing, 0o640)
            atomic_write_utf8(str(existing), "new\n")
            self.assertEqual(stat.S_IMODE(existing.stat().st_mode), 0o640)
            new = Path(tmp) / "new.md"
            atomic_write_utf8(str(new), "new\n")
            self.assertEqual(stat.S_IMODE(new.stat().st_mode), 0o600)

    def test_nonregular_library_targets_fail_visibly_without_blocking(self):
        with tempfile.TemporaryDirectory() as tmp:
            candidates = []
            directory = Path(tmp) / "directory"
            directory.mkdir()
            candidates.append(directory)
            if hasattr(os, "mkfifo"):
                fifo = Path(tmp) / "fifo"
                os.mkfifo(fifo)
                candidates.append(fifo)
            if hasattr(socket, "AF_UNIX"):
                sock_path = Path(tmp) / "sock"
                sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                try:
                    sock.bind(str(sock_path))
                    candidates.append(sock_path)
                    for candidate in candidates:
                        snapshot = MarkdownReferenceStore(str(candidate)).load()
                        self.assertFalse(snapshot.writable)
                        self.assertTrue(snapshot.diagnostics)
                finally:
                    sock.close()
            else:
                for candidate in candidates:
                    snapshot = MarkdownReferenceStore(str(candidate)).load()
                    self.assertFalse(snapshot.writable)
                    self.assertTrue(snapshot.diagnostics)

    def test_external_change_before_save_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "references.md"
            store = MarkdownReferenceStore(str(path))
            first = store.save((self.record("First"),), store.load().token)
            self.assertTrue(first.saved)
            path.write_text(path.read_text(encoding="utf-8") + "\nexternal\n", encoding="utf-8")
            blocked = store.save((self.record("Second"),), first.token)
            self.assertEqual(blocked.status, "conflict")

    def test_change_during_write_before_replace_blocks_and_preserves_external_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "references.md"
            store = MarkdownReferenceStore(str(path))
            first = store.save((self.record("First"),), store.load().token)
            self.assertTrue(first.saved)
            real_mkstemp = tempfile.mkstemp
            changed = False
            def mutate_after_temp(*args, **kwargs):
                nonlocal changed
                result = real_mkstemp(*args, **kwargs)
                if not changed:
                    path.write_text("# Calamus References v1\n\n## external\nTitle: External\n", encoding="utf-8")
                    changed = True
                return result
            with mock.patch("schedulae.research_file.tempfile.mkstemp", side_effect=mutate_after_temp):
                result = store.save((self.record("Second"),), first.token)
            self.assertEqual(result.status, "conflict")
            self.assertIn("External", path.read_text(encoding="utf-8"))

    def test_writer_failure_preserves_previous_library_and_cleans_owned_temp(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "references.md"
            atomic_write_utf8(str(path), "before\n")
            before = path.read_bytes()
            with mock.patch("schedulae.research_file.os.replace", side_effect=OSError("replace failed")):
                with self.assertRaises(OSError):
                    atomic_write_utf8(str(path), "after\n")
            self.assertEqual(path.read_bytes(), before)
            leftovers = list(Path(tmp).glob(".references.md.schedulae-*.tmp"))
            self.assertEqual(leftovers, [])

    def test_file_token_rejects_nonregular_instead_of_reporting_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp) / "dir"
            directory.mkdir()
            with self.assertRaises(OSError):
                file_token(str(directory))


if __name__ == "__main__":
    unittest.main()

# SPDX-License-Identifier: GPL-3.0-or-later
"""GTK-free standalone bibliography projections and immutable operation plans."""
from __future__ import annotations

from dataclasses import dataclass, replace
import os
from typing import Iterable

from schedulae.related_references import related_keys, related_reference_issues
from schedulae.references import ReferenceRecord, suggest_reference_key

_SORTS = ("author-year-title", "title", "year", "key", "type")


@dataclass(frozen=True)
class BibliographyFilters:
    query: str = ""
    reference_type: str = "all"
    tag: str = "all"
    file: str = "all"
    integrity: str = "all"
    sort: str = "author-year-title"

    def __post_init__(self) -> None:
        if self.file not in {"all", "present", "missing", "unset"}:
            raise ValueError("bibliography file filter is invalid")
        if self.integrity not in {"all", "error", "warning", "clean"}:
            raise ValueError("bibliography integrity filter is invalid")
        if self.sort not in _SORTS:
            raise ValueError("bibliography sort is invalid")


@dataclass(frozen=True)
class BibliographyContext:
    issue_severities_by_key: tuple[tuple[str, tuple[str, ...]], ...] = ()

    def severities(self, key: str) -> tuple[str, ...]:
        return dict(self.issue_severities_by_key).get(key, ())


@dataclass(frozen=True)
class ReferenceDeleteImpact:
    key: str
    related_reference_owners: tuple[str, ...] = ()

    @property
    def used(self) -> bool:
        return bool(self.related_reference_owners)

    @property
    def summary_lines(self) -> tuple[str, ...]:
        if not self.related_reference_owners:
            return ()
        return ("Related from: " + ", ".join(self.related_reference_owners),)


def complete_search_text(record: ReferenceRecord) -> str:
    if not isinstance(record, ReferenceRecord):
        raise TypeError("record must be ReferenceRecord")
    values = (
        "key", record.key, "aliases", *record.aliases, "title", record.title,
        "type", record.type, "year", record.year, "author", *record.authors,
        "editor", *record.editors, "container", record.container_title,
        "publisher", record.publisher, "location", record.location,
        "volume", record.volume, "issue", record.issue, "pages", record.pages,
        "doi", record.doi, "isbn", record.isbn, "issn", record.issn,
        "url", record.url, "language", record.language, "file", record.file_path,
        "tags", *record.tags, "annotation", record.annotation,
        *(item for pair in record.extra_fields for item in pair),
    )
    return "\n".join(values).casefold()


def available_types(records: Iterable[ReferenceRecord]) -> tuple[str, ...]:
    return tuple(sorted({record.type for record in records}, key=str.casefold))


def available_tags(records: Iterable[ReferenceRecord]) -> tuple[str, ...]:
    display: dict[str, str] = {}
    for record in records:
        for tag in record.tags:
            display.setdefault(tag.casefold(), tag)
    return tuple(display[key] for key in sorted(display))


def file_state(record: ReferenceRecord) -> str:
    if not record.file_path:
        return "unset"
    return "present" if os.path.exists(os.path.expanduser(record.file_path)) else "missing"


def project_references(
    records: Iterable[ReferenceRecord],
    filters: BibliographyFilters = BibliographyFilters(),
    context: BibliographyContext = BibliographyContext(),
) -> tuple[ReferenceRecord, ...]:
    snapshot = tuple(records)
    if any(not isinstance(record, ReferenceRecord) for record in snapshot):
        raise TypeError("records must contain ReferenceRecord values")
    needle = filters.query.strip().casefold()
    visible: list[ReferenceRecord] = []
    for record in snapshot:
        if needle and needle not in complete_search_text(record):
            continue
        if filters.reference_type != "all" and record.type != filters.reference_type:
            continue
        if filters.tag != "all" and filters.tag.casefold() not in {tag.casefold() for tag in record.tags}:
            continue
        if filters.file != "all" and file_state(record) != filters.file:
            continue
        severities = set(context.severities(record.key))
        if filters.integrity == "clean" and severities:
            continue
        if filters.integrity not in {"all", "clean"} and filters.integrity not in severities:
            continue
        visible.append(record)

    def sortable(value: str) -> tuple[int, str]:
        folded = value.strip().casefold()
        return (0, folded) if folded else (1, "")

    def key(record: ReferenceRecord):
        if filters.sort == "title":
            return (sortable(record.title), sortable(record.key))
        if filters.sort == "year":
            return (sortable(record.year), sortable(record.primary_author), sortable(record.title), sortable(record.key))
        if filters.sort == "key":
            return (sortable(record.key),)
        if filters.sort == "type":
            return (sortable(record.type), sortable(record.primary_author), sortable(record.title), sortable(record.key))
        return (sortable(record.primary_author), sortable(record.year), sortable(record.title), sortable(record.key))

    return tuple(sorted(visible, key=key))


def duplicate_reference(record: ReferenceRecord, existing_identity_keys: Iterable[str]) -> ReferenceRecord:
    if not isinstance(record, ReferenceRecord):
        raise TypeError("record must be ReferenceRecord")
    key = suggest_reference_key(record.authors, record.year, record.title, existing_identity_keys)
    return replace(record, key=key, aliases=())


def build_delete_impact(records: Iterable[ReferenceRecord], key: str) -> ReferenceDeleteImpact:
    snapshot = tuple(records)
    target = next((record for record in snapshot if record.key == key), None)
    if target is None:
        raise ValueError("reference is not available")
    identities = set(target.identity_keys)
    related_owners = tuple(
        record.key for record in snapshot
        if record.key != key and identities.intersection(related_keys(record))
    )
    return ReferenceDeleteImpact(key=key, related_reference_owners=related_owners)


def format_reference_detail(
    record: ReferenceRecord,
    context: BibliographyContext = BibliographyContext(),
) -> str:
    fields: list[tuple[str, str]] = [
        ("Key", record.key),
        ("Aliases", ", ".join(record.aliases)),
        ("Type", record.type),
        ("Author", "; ".join(record.authors)),
        ("Editor", "; ".join(record.editors)),
        ("Title", record.title),
        ("Year / Date", record.year),
        ("Container", record.container_title),
        ("Publisher", record.publisher),
        ("Location", record.location),
        ("Volume", record.volume),
        ("Issue", record.issue),
        ("Pages", record.pages),
        ("DOI", record.doi),
        ("ISBN", record.isbn),
        ("ISSN", record.issn),
        ("URL", record.url),
        ("Language", record.language),
        ("Tags", ", ".join(record.tags)),
        ("Local File", record.file_path),
        ("File Status", file_state(record)),
        ("Related", ", ".join(related_keys(record))),
        ("Integrity", ", ".join(context.severities(record.key)) or "clean"),
    ]
    fields.extend(record.extra_fields)
    body = "\n".join(f"{label}: {value}" for label, value in fields if value)
    if record.annotation:
        body += "\n\nAnnotation\n" + record.annotation
    return body


def render_plain_bibliography(records: Iterable[ReferenceRecord]) -> str:
    lines: list[str] = []
    for record in records:
        author = "; ".join(record.authors) or "Unknown author"
        year = f" ({record.year})" if record.year else ""
        publication = ". ".join(value for value in (record.location, record.publisher) if value)
        line = f"{author}{year}. {record.title}."
        if publication:
            line += f" {publication}."
        lines.append(line)
    return "\n".join(lines) + ("\n" if lines else "")


def render_markdown_bibliography(records: Iterable[ReferenceRecord]) -> str:
    plain = render_plain_bibliography(records).splitlines()
    return "# Bibliography\n\n" + "\n".join(f"- {line}" for line in plain) + ("\n" if plain else "")


def _normalized_identifier(value: str) -> str:
    return "".join(char for char in value.casefold() if char.isalnum())


def build_bibliography_context(records: Iterable[ReferenceRecord]) -> BibliographyContext:
    snapshot = tuple(records)
    if any(not isinstance(record, ReferenceRecord) for record in snapshot):
        raise TypeError("records must contain ReferenceRecord values")

    identifiers: dict[tuple[str, str], list[str]] = {}
    for record in snapshot:
        for kind, value in (("doi", record.doi), ("isbn", record.isbn), ("issn", record.issn)):
            normalized = _normalized_identifier(value)
            if normalized:
                identifiers.setdefault((kind, normalized), []).append(record.key)

    severities: dict[str, set[str]] = {record.key: set() for record in snapshot}
    for record in snapshot:
        if record.file_path and file_state(record) == "missing":
            severities[record.key].add("warning")
        for kind, value in (("doi", record.doi), ("isbn", record.isbn), ("issn", record.issn)):
            normalized = _normalized_identifier(value)
            if normalized and len(identifiers.get((kind, normalized), ())) > 1:
                severities[record.key].add("error")

    for issue in related_reference_issues(snapshot):
        severities.setdefault(issue.subject_key, set()).add(issue.severity)

    return BibliographyContext(
        issue_severities_by_key=tuple(
            (key, tuple(sorted(values))) for key, values in severities.items()
        )
    )

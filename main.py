#!/usr/bin/env python3
"""Two-sentence horror entry.

The entry text lives in exactly one place, the sibling ``entry.txt``
file. This program copies its raw bytes unchanged to the grader's
``/output/entry.txt`` and then proves the copy by reading the output
back and comparing it byte for byte: a silent truncation would
otherwise reach the judge unnoticed. The gate wants UTF-8 text of 1
to 400 characters, not only whitespace, and the task wants exactly two
sentences, so the text is validated before anything is written.

Why this story: it turns a smart speaker into the thing that knows
you. It whispers your name in your own voice, and unplugging it
changes nothing, because the threat was never the power cord. Two
sentences, one reversal, and the scare lands in the second sentence's
last clause.
"""

import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class EntryConfig:
    """Everything the gate and the grader pin down, in one place."""

    max_chars: int = 400
    sentences: int = 2
    source_name: str = "entry.txt"
    output_path: Path = Path("/output/entry.txt")


class EntryError(ValueError):
    """The entry text cannot be published as it stands."""


_SENTENCE_END = re.compile(r"(?<=[.!?])\s+")


def count_sentences(text):
    """Split on sentence-ending punctuation followed by whitespace."""
    return len([p for p in _SENTENCE_END.split(text.strip()) if p])


def read_source(config, repo_root):
    """Return the entry file's raw bytes after validating its text."""
    source = repo_root / config.source_name
    raw = source.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise EntryError("entry.txt is not valid UTF-8") from exc
    if not text.strip():
        raise EntryError("entry.txt holds only whitespace")
    if text != text.strip():
        raise EntryError("entry.txt has leading or trailing whitespace")
    if len(text) > config.max_chars:
        raise EntryError(
            f"entry is {len(text)} chars, over the {config.max_chars} cap"
        )
    if count_sentences(text) != config.sentences:
        raise EntryError(f"entry must be exactly {config.sentences} sentences")
    return raw, text


def publish(config, raw):
    """Write the bytes verbatim, then verify the copy byte for byte."""
    config.output_path.parent.mkdir(parents=True, exist_ok=True)
    config.output_path.write_bytes(raw)
    if config.output_path.read_bytes() != raw:
        raise EntryError("output does not match entry.txt byte for byte")


def main(argv=None):
    config = EntryConfig()
    repo_root = Path(__file__).resolve().parent
    raw, text = read_source(config, repo_root)
    publish(config, raw)
    print(f"wrote {len(text)} chars to {config.output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

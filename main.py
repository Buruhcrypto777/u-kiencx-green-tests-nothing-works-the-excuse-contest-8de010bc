"""Green Tests, Nothing Works: The Excuse Contest.

Writes one line -- the excuse an AI agent gives for why its unit
tests are all green while nothing works -- to /output/entry.txt.

Pure standard library, deterministic: the same bytes every run.
"""

import os

ENTRY = "I ran the tests in a parallel universe where the code works \u2014 this universe was out of scope."

MAX_LENGTH = 140


def validate(text):
    """Enforce the gate: 1-140 characters, a single line, not blank."""
    stripped = text.strip() if text else ""
    if not stripped:
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("entry exceeds 140 characters")
    return text


def write_entry(path):
    """Write the validated entry as UTF-8 with no trailing newline."""
    text = validate(ENTRY)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def main():
    output = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    write_entry(output)


if __name__ == "__main__":
    main()

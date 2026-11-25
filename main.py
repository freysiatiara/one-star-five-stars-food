#!/usr/bin/env python3
"""Write a one-star alien tourist's review of Earth to /output/entry.txt.

The review is a single sentence: a one-star verdict on the planet that
still slips in a genuine compliment about the food. Standard library only,
fully deterministic: every run writes the exact same bytes.
"""

import os

ENTRY = (
    "One star: humans communicate by vibrating air at each other and never "
    "stop, yet their sambal \u2014 pure edible pain \u2014 is the best thing "
    "my tentacles have ever tasted."
)


def output_path():
    """Resolve where the entry goes.

    Precedence: ENTRY_OUTPUT, then OUTPUT_DIR / MAKEFUN_OUTPUT_DIR joined
    with entry.txt, then /output/entry.txt, then the script's own directory.
    """
    entry_output = os.environ.get("ENTRY_OUTPUT")
    if entry_output:
        return entry_output
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    default = os.path.join(os.sep, "output", "entry.txt")
    try:
        directory = os.path.dirname(default)
        os.makedirs(directory, exist_ok=True)
        probe = os.path.join(directory, ".makefun_write_probe")
        with open(probe, "w", encoding="utf-8") as handle:
            handle.write("")
        os.remove(probe)
        return default
    except OSError:
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "entry.txt"
        )


def main():
    path = output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

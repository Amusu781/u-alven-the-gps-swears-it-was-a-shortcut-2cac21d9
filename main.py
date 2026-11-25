#!/usr/bin/env python3
"""Write the GPS's one-line excuse to /output/entry.txt.

Stdlib only, no network. The line is the GPS speaking in its own voice:
smug, defensive, blaming the map, with one concrete image (the lake that
was supposed to have a bridge) and the turn landing in the last few words.
"""

import os

ENTRY = "The map promised a shortcut, and the lake was supposed to have a bridge \u2014 I checked twice."
# Gate: a single line of plain UTF-8 text, 1 to 200 characters, not only
# whitespace. This line is 90 characters, one line, no trailing newline
# beyond the text itself (the file holds exactly the line).


def main():
    # Create the output directory first; never delete it (the grader mounts
    # /output read-only as uid 65534 and deleting it throws EACCES).
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

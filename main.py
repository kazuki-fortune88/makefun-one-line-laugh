"""One Line, One Laugh entry.

Writes a single funny line to entry.txt in the output directory
(default /output, or $MAKEFUN_OUTPUT_DIR when set).
"""

import os

LINE = "My smartwatch congratulated me on 10,000 steps \u2014 all of them from pacing to avoid a phone call."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Never remove the output directory itself: on the grader it is a
    # mount point. Just create it if it does not exist yet.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

The word: Ghosting.
Home Wi-Fi ghosts you: full bars one second, gone the next, right in the
middle of the call that mattered. Funny at once, true to how it actually
behaves, and it even works as a network name.
"""

import os

WORD = "Ghosting"


def main() -> None:
    print(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

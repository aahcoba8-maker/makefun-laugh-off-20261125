"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt (MAKEFUN_OUTPUT_DIR
when set, otherwise the script directory). Stdlib only.
"""

import os

ENTRY = "I gave my AI a day off. It spent it learning my job."


def main():
    # Gate: entry must be 1-200 chars of non-whitespace UTF-8 text.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

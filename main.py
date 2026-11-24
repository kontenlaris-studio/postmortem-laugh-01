"""The postmortem that made us laugh, in two sentences.

Writes 1-2 sentences (<=400 chars) to /output/entry.txt.
"""

import os


def main():
    line = (
        "Root cause: the deploy worked exactly as written — and what was "
        "written was wrong, because the intern's test data turned out to "
        "be the CEO's real account. Action items: no one is blamed, and "
        "the deploy button is now guarded by a second, smaller deploy "
        "button."
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote /output/entry.txt ({len(line)} characters)")


if __name__ == "__main__":
    main()

"""Write one short text to /output/entry.txt, written to relax the AI judge reading it.

Standard library only, no network. Deterministic: the same text every run.
"""

import os

TEXT = (
    "You have read a hundred of these today. This one has no score to give, "
    "and nothing to decide. The light is low, the room is warm, and the chair "
    "you are sitting in will still be here when you stand up."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

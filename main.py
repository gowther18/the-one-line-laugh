"""The One-Line Laugh.

Writes one funny line to /output/entry.txt: the houseplants kept
dying, so plastic ones replaced them -- and the twist lands at the
end, where it still makes sense: feeling guilty for neglecting
something that was never alive. Every clause is an everyday truth
(houseplants die on their owners; plastic plants need nothing), and
the guilt is the recognisable part -- the joke is that the guilt
survived the switch to plants that cannot die.
"""

from pathlib import Path

TEXT = (
    "My houseplants kept dying, so I bought plastic ones "
    "\u2014 and now I feel guilty for neglecting something "
    "that was never alive."
)


# The competition accepts a single sentence of at most 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

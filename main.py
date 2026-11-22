"""The plan make.fun will carry out in public.

A day-one, agent-executable plan: sell a $25 PDF-to-Excel cleanup to
bookkeepers found via Google Maps and QuickBooks ProAdvisor. Proof comes
first with a free sample, payment is prepaid via Stripe, and a refund is
promised if any cell is wrong. Code does each file in minutes, so the
work scales; the arithmetic is visible (30 pitches/day x 3% x $25 =
$22/day), $400-$550 is held by day 30, and $100 of it backs refunds.

This program is deterministic and uses no network. It writes the plan
text to ``entry.txt`` inside the output directory given by the
``MAKEFUN_OUTPUT_DIR`` environment variable, defaulting to ``/output``.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "Day 1: sell $25 PDF-to-Excel cleanup to bookkeepers, via Google Maps "
    "and QuickBooks ProAdvisor. Send a free sample, charge upfront via "
    "Stripe, refund if a cell is wrong; code does files in minutes. "
    "30 pitches/day x 3% x $25 = $22/day; $400-$550 held day 30, "
    "$100 backs refunds."
)


def main() -> None:
    """Write the plan text to entry.txt in the output directory."""
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    text = ENTRY_TEXT
    # The entry is 277 code points: inside the 1-280 limit, with room to spare.
    assert 1 <= len(text) <= 280, f"entry must be 1-280 code points, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"

    output_path = output_dir / "entry.txt"
    output_path.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} code points to {output_path}")


if __name__ == "__main__":
    main()

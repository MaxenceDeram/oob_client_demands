"""
Utility helpers for oob_client_demands to enable testing and reuse.
Functions are small, pure, and avoid changing repository files.
"""
from typing import List


def read_csv_rows(filepath: str) -> List[List[str]]:
    """Read a CSV-like file (first line is header) and return list of rows (as lists of strings)."""
    with open(filepath, "r") as f:
        lines = f.readlines()
    if not lines:
        return []
    # Skip header row
    rows = [line.strip().split(",") for line in lines[1:]]
    return rows


def next_id_from_file(filepath: str) -> int:
    """Return the "next id" the project uses (number of lines in the file).

    This mirrors the project's current behavior where IDs are created via
    `new_id = len(open(file).readlines())` and includes the header line in the count.
    """
    with open(filepath, "r") as f:
        lines = f.readlines()
    return len(lines)


def parse_amount_from_row(row: List[str], index: int = 2) -> float:
    """Parse a numeric amount from a CSV row (by column index)."""
    if len(row) <= index:
        raise ValueError("missing amount column")
    return float(row[index])


def sum_column(filepath: str, index: int = 2) -> float:
    """Sum a numeric column (default: column index 2) across data rows in the file."""
    total = 0.0
    for row in read_csv_rows(filepath):
        try:
            total += parse_amount_from_row(row, index)
        except ValueError:
            # Skip rows that don't have the expected columns.
            continue
    return total

import os
import oob_utils as u

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")


def test_read_csv_rows_invoices():
    invoices = u.read_csv_rows(os.path.join(FIXTURES, "invoices.txt"))
    assert len(invoices) == 2
    assert invoices[0][2] == "100.00"


def test_parse_amount_from_row():
    row = ["1", "1", "150.50", "2025-02-01", "Consulting"]
    assert u.parse_amount_from_row(row) == 150.50


def test_sum_column_invoices():
    total = u.sum_column(os.path.join(FIXTURES, "invoices.txt"))
    assert abs(total - 250.50) < 1e-6


def test_sum_column_expenses():
    total = u.sum_column(os.path.join(FIXTURES, "expenses.txt"))
    assert abs(total - 250.00) < 1e-6

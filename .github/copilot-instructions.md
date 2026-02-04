# Copilot instructions for oob_client_demands ✅

## Big picture
- This is a small, educational CLI bookkeeping project. Each top-level script is a standalone command-line tool (no packages): `clients.py`, `invoices.py`, `expenses.py`, `summary.py`, `vat_calculator.py`.
- Data persistence is plain CSV-like text files in the repo root: `clients.txt`, `invoices.txt`, `expenses.txt`. Files are initialized with a header (e.g. `id,name,email`).
- Typical data flow: Users add clients → create invoices (reference `client_id`) → `summary.py` reads `invoices.txt` and `expenses.txt` to compute net profit.

## Key conventions & patterns 🔧
- Files are treated as append-only CSVs with a header line. Example headers:
  - `clients.txt` → `id,name,email`
  - `invoices.txt` → `id,client_id,amount,date,description`
  - `expenses.txt` → `id,category,amount,date,description`
- New IDs are created by counting lines in the file (i.e. `new_id = len(open(file).readlines())`).
- Scripts use imperative top-level code + input() loops (no functions / classes by design). When refactoring, keep behavior identical and add tests.
- Numeric values are stored as plain decimal strings (e.g., `150.50`) and read with `float()` in `summary.py`.

## What to watch out for (practical rules) ⚠️
- Preserve header line and CSV order when editing or migrating data. Tests and scripts assume specific column positions.
- `client_id` is a live reference ID — adding/removing lines changes IDs if the current scheme is altered. If you change ID strategy, update `invoices.py` and `summary.py` together.
- Many places don't validate user input (e.g., numeric parsing, date format). If adding validation, be explicit and include unit tests and examples in the README.
- Use the `csv` stdlib when converting code from manual `split(',')` logic to avoid issues with commas in fields.

## Guidance for changes & PRs ✅
- Small, behavior-preserving refactors are preferred. Example safe refactors:
  - Extract repeated file read/write patterns into helper functions.
  - Replace naive `split(',')` with `csv.reader` but keep the header handling identical.
- When introducing ID changes or schema changes, include a migration script and update `README.md` to explain the new file format.
- Add unit tests (pytest) when you add logic beyond trivial IO (new validation rules, calculations, or refactors). Add sample test data files under `tests/fixtures/`.

## How to run & debug 🧪
- Run individual scripts directly: `python3 clients.py`, `python3 invoices.py`, `python3 expenses.py`, `python3 summary.py`, `python3 vat_calculator.py`.
- To inspect data, open `*.txt` files in editor; they are human-readable CSVs.
- For debugging numeric issues, run `summary.py` and check for ValueError on `float()` conversion; add robust parsing when necessary.

## Examples to reference in-code
- ID generation: see `clients.py` and `invoices.py` where `new_id = len(all_lines)` is used before appending.
- Aggregation: `summary.py` reads `invoices.txt` and sums the third CSV column as income (i.e., `parts[2]`).

## Testing & CI ✅
- Unit tests use `pytest`. Example command: `python -m pytest -q` or `pytest -q`.
- To install local dev dependencies quickly: `python -m pip install -r dev-requirements.txt`.
- Tests live under `tests/` and example fixtures are under `tests/fixtures/` (e.g., `tests/fixtures/invoices.txt`).
- A small helper module `oob_utils.py` contains parsing and aggregation helpers intended for unit tests.
- When adding behavior (validation, parsing, migrations), include focused unit tests that assert parsing and aggregation logic using the fixtures.

> Note: A minimal GitHub Actions workflow (`.github/workflows/ci.yml`) is included to install dev requirements and run the test suite + `summary.py` — adapt Python version and matrix as needed.

---
Please review these instructions for accuracy or missing project-specific details. Tell me which sections you want expanded or examples you'd like added and I will update the file. ✨
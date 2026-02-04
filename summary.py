# ==========================================
# FINANCIAL SUMMARY - FUNCTIONAL VERSION
# ==========================================

INVOICE_DATA = "invoices.txt"
EXPENSE_DATA = "expenses.txt"


# --- FUNCTIONS ---
def sum_csv_column(filename, column_index):
    total = 0.0
    try:
        f = open(filename, "r")
        f.readline()  # skip header

        line = f.readline()
        while line:
            parts = line.strip().split(",")
            if len(parts) > column_index:
                total = total + float(parts[column_index])
            line = f.readline()

        f.close()
    except:
        total = 0.0

    return total


def calculate_profit(income, expenses):
    return income - expenses


def display_summary(income, expenses, result):
    print("\n" + "=" * 35)
    print("      YEAR-TO-DATE SUMMARY")
    print("=" * 35)
    print("Total Gross Income:   $" + format(income, "10.2f"))
    print("Total Business Costs: $" + format(expenses, "10.2f"))
    print("-" * 35)

    if result >= 0:
        print("NET PROFIT:          +$" + format(result, "10.2f"))
    else:
        print("NET LOSS:            -$" + format(abs(result), "10.2f"))

    print("=" * 35)


# --- PROGRAM START ---
print("Reading Invoice data...")
income_total = sum_csv_column(INVOICE_DATA, 2)

print("Reading Expense data...")
expense_total = sum_csv_column(EXPENSE_DATA, 2)

profit_or_loss = calculate_profit(income_total, expense_total)

display_summary(income_total, expense_total, profit_or_loss)
print("End of Summary.")
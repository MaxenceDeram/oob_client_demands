# ==========================================
# FINANCIAL SUMMARY - EDUCATIONAL VERSION
# ==========================================
# This script "pulls it all together".
# It reads both Invoices and Expenses to calculate the Net Profit.
# Students: Observe how we reuse the file-reading pattern here!

INVOICE_DATA = "invoices.txt"
EXPENSE_DATA = "expenses.txt"

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
        # file missing or data problem
        total = 0.0
    return total


print("Reading Invoice data...")
income_total = sum_csv_column(INVOICE_DATA, 2)   # amount is column 2

print("Reading Expense data...")
expense_total = sum_csv_column(EXPENSE_DATA, 2)  # amount is column 2

profit_or_loss = income_total - expense_total

print("\n" + "="*35)
print("      YEAR-TO-DATE SUMMARY")
print("="*35)
print("Total Gross Income:   $" + format(income_total, "10.2f"))
print("Total Business Costs: $" + format(expense_total, "10.2f"))
print("-" * 35)

if profit_or_loss >= 0:
    print("NET PROFIT:          +$" + format(profit_or_loss, "10.2f"))
else:
    print("NET LOSS:            -$" + format(abs(profit_or_loss), "10.2f"))

print("="*35)

# Strictly Imperative Financial Summary
# No imports, no functions

INVOICE_FILE = "invoices.txt"
EXPENSE_FILE = "expenses.txt"

total_income = 0.0
total_expenses = 0.0

# Manual parsing for Invoices
try:
    f = open(INVOICE_FILE, "r")
    header = f.readline()
    line = f.readline()
    while line:
        parts = []
        current_part = ""
        for char in line:
            if char == "," or char == "\n":
                parts.append(current_part)
                current_part = ""
            else:
                current_part += char
        
        if len(parts) >= 3:
            try:
                total_income += float(parts[2])
            except ValueError:
                pass
        line = f.readline()
    f.close()
except FileNotFoundError:
    pass

# Manual parsing for Expenses
try:
    f = open(EXPENSE_FILE, "r")
    header = f.readline()
    line = f.readline()
    while line:
        parts = []
        current_part = ""
        for char in line:
            if char == "," or char == "\n":
                parts.append(current_part)
                current_part = ""
            else:
                current_part += char
        
        if len(parts) >= 3:
            try:
                total_expenses += float(parts[2])
            except ValueError:
                pass
        line = f.readline()
    f.close()
except FileNotFoundError:
    pass

net_result = total_income - total_expenses

print("\n" + "="*30)
print("      FINANCIAL SUMMARY      ")
print("="*30)
print("Total Income:     " + str(round(total_income, 2)))
print("Total Expenses:   " + str(round(total_expenses, 2)))
print("-" * 30)
print("Net Result:       " + str(round(net_result, 2)))
print("="*30 + "\n")

# Strictly Imperative VAT Calculator
# No imports, no functions

print("--- VAT CALCULATOR ---")

raw_amount = input("Enter net amount: ")
raw_rate = input("Enter VAT rate (default 20%): ")

# Manual conversion and default handling
try:
    amount = float(raw_amount)
    if raw_rate == "":
        rate = 20.0
    else:
        rate = float(raw_rate)
    
    vat_amount = amount * (rate / 100.0)
    total = amount + vat_amount
    
    # Manual rounding to 2 decimal places for output
    print("VAT Amount (" + str(rate) + "%): " + str(round(vat_amount, 2)))
    print("Total Amount (incl. VAT): " + str(round(total, 2)))
except ValueError:
    print("Error: Please enter valid numbers.")

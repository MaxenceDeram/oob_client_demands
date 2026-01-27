# Strictly Imperative Invoice Management
# No imports, no functions

FILENAME = "invoices.txt"

# Create file if it doesn't exist
try:
    f = open(FILENAME, "r")
    f.close()
except FileNotFoundError:
    f = open(FILENAME, "w")
    f.write("id,client_id,amount,date,description\n")
    f.close()

while True:
    print("\n--- INVOICE MANAGEMENT ---")
    print("1. Add Invoice")
    print("2. List Invoices")
    print("3. Exit")
    choice = input("Select an option: ")
    
    if choice == '1':
        client_id = input("Enter client ID: ")
        amount = input("Enter amount: ")
        date = input("Enter date (YYYY-MM-DD): ")
        desc = input("Enter description: ")
        
        # Calculate next ID
        f = open(FILENAME, "r")
        lines = f.readlines()
        f.close()
        next_id = len(lines)
        
        # Append data
        f = open(FILENAME, "a")
        f.write(str(next_id) + "," + client_id + "," + amount + "," + date + "," + desc + "\n")
        f.close()
        print("Invoice added for client " + client_id + " (Amount: " + amount + ")")
        
    elif choice == '2':
        print("\n--- INVOICE LIST ---")
        f = open(FILENAME, "r")
        header = f.readline() # Skip header
        line = f.readline()
        while line:
            # Manual CSV parsing
            parts = []
            current_part = ""
            for char in line:
                if char == "," or char == "\n":
                    parts.append(current_part)
                    current_part = ""
                else:
                    current_part += char
            
            if len(parts) >= 5:
                print("ID: " + parts[0] + " | Client: " + parts[1] + " | Amount: " + parts[2] + " | Date: " + parts[3] + " | Desc: " + parts[4])
            line = f.readline()
        f.close()
        print("--------------------\n")
        
    elif choice == '3':
        break
    else:
        print("Invalid choice.")

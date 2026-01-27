# Strictly Imperative Client Management
# No imports, no functions

FILENAME = "clients.txt"

# Create file if it doesn't exist
try:
    f = open(FILENAME, "r")
    f.close()
except FileNotFoundError:
    f = open(FILENAME, "w")
    f.write("id,name,email\n")
    f.close()

while True:
    print("\n--- CLIENT MANAGEMENT ---")
    print("1. Add Client")
    print("2. List Clients")
    print("3. Exit")
    choice = input("Select an option: ")
    
    if choice == '1':
        name = input("Enter client name: ")
        email = input("Enter client email: ")
        
        # Calculate next ID
        f = open(FILENAME, "r")
        lines = f.readlines()
        f.close()
        next_id = len(lines)
        
        # Append data
        f = open(FILENAME, "a")
        f.write(str(next_id) + "," + name + "," + email + "\n")
        f.close()
        print("Client " + name + " added with ID " + str(next_id))
        
    elif choice == '2':
        print("\n--- CLIENT LIST ---")
        f = open(FILENAME, "r")
        header = f.readline() # Skip header
        line = f.readline()
        while line:
            # Manual CSV parsing (assuming no commas in names/emails for simplicity)
            parts = []
            current_part = ""
            for char in line:
                if char == "," or char == "\n":
                    parts.append(current_part)
                    current_part = ""
                else:
                    current_part += char
            
            if len(parts) >= 3:
                print("ID: " + parts[0] + " | Name: " + parts[1] + " | Email: " + parts[2])
            line = f.readline()
        f.close()
        print("-------------------\n")
        
    elif choice == '3':
        break
    else:
        print("Invalid choice.")

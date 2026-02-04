# ==========================================
# CLIENT MANAGEMENT - BASIC VERSION
# ==========================================

FILENAME = "clients.txt"

# --- 1. INITIALIZATION ---
try:
    file = open(FILENAME, "r")
    file.close()
except:
    print("Initializing database...")
    file = open(FILENAME, "w")
    file.write("id,name,email\n")
    file.close()


# --- 2. MAIN MENU LOOP ---
while True:
    print("\n=========================")
    print("   CLIENT MANAGEMENT")
    print("=========================")
    print("1. Add a New Client")
    print("2. View All Clients")
    print("3. Exit Program")
    print("-------------------------")

    choice = input("What would you like to do? ")

    # --- 3. ADD CLIENT + PROFILE ---
    if choice == "1":
        print("\nAdding a new client...")
        name = input("Name: ")
        email = input("Email: ")

        # Get next ID
        file = open(FILENAME, "r")
        lines = file.readlines()
        file.close()

        new_id = len(lines)

        # Save client
        file = open(FILENAME, "a")
        file.write(str(new_id) + "," + name + "," + email + "\n")
        file.close()

        # --- CLIENT PROFILE ---
        print("\n=========================")
        print("     CLIENT PROFILE")
        print("=========================")
        print("ID    :", new_id)
        print("Name  :", name)
        print("Email :", email)
        print("=========================")
        print("Client created successfully.")

    # --- 4. VIEW CLIENTS ---
    elif choice == "2":
        print("\n------ CLIENT LIST ------")

        file = open(FILENAME, "r")
        file.readline()  # skip header

        line = file.readline()
        while line:
            parts = line.strip().split(",")

            print(
                "ID:", parts[0],
                "| Name:", parts[1],
                "| Email:", parts[2]
            )

            line = file.readline()

        file.close()
        print("-------------------------")

    # --- 5. EXIT ---
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2 or 3.")

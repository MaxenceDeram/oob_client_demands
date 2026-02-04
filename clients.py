# ==========================================
# CLIENT MANAGEMENT 
# ==========================================

FILENAME = "clients.txt"


# --- FUNCTIONS ---
def init_file():
    try:
        f = open(FILENAME, "r")
        f.close()
    except:
        print("Initializing database...")
        f = open(FILENAME, "w")
        f.write("id,name,email\n")
        f.close()


def read_all_lines():
    f = open(FILENAME, "r")
    lines = f.readlines()
    f.close()
    return lines


def get_next_id():
    lines = read_all_lines()
    return len(lines)


def append_client(client_id, name, email):
    f = open(FILENAME, "a")
    f.write(str(client_id) + "," + name + "," + email + "\n")
    f.close()


def show_client_profile(client_id, name, email):
    print("\n=========================")
    print("     CLIENT PROFILE")
    print("=========================")
    print("ID    :", client_id)
    print("Name  :", name)
    print("Email :", email)
    print("=========================")


def display_clients():
    print("\n------ CLIENT LIST ------")

    f = open(FILENAME, "r")
    f.readline()  # skip header

    line = f.readline()
    while line:
        parts = line.strip().split(",")

        if len(parts) >= 3:
            print("ID:", parts[0], "| Name:", parts[1], "| Email:", parts[2])

        line = f.readline()

    f.close()
    print("-------------------------")


# --- PROGRAM START ---
init_file()

while True:
    print("\n=========================")
    print("   CLIENT MANAGEMENT")
    print("=========================")
    print("1. Add a New Client")
    print("2. View All Clients")
    print("3. Exit Program")
    print("-------------------------")

    choice = input("What would you like to do? ")

    if choice == "1":
        print("\nAdding a new client...")
        name = input("Name: ")
        email = input("Email: ")

        new_id = get_next_id()
        append_client(new_id, name, email)

        show_client_profile(new_id, name, email)
        print("Client created successfully.")

    elif choice == "2":
        display_clients()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2 or 3.")
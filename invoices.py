# ==========================================
# INVOICE MANAGEMENT - FUNCTIONAL VERSION
# ==========================================

FILENAME = "invoices.txt"


# --- FUNCTIONS ---
def init_file():
    try:
        f = open(FILENAME, "r")
        f.close()
    except:
        f = open(FILENAME, "w")
        f.write("id,client_id,amount,date,description\n")
        f.close()


def read_all_lines():
    f = open(FILENAME, "r")
    lines = f.readlines()
    f.close()
    return lines


def get_next_id():
    lines = read_all_lines()
    return len(lines)


def append_invoice(data_line):
    f = open(FILENAME, "a")
    f.write(data_line)
    f.close()


def display_invoices():
    f = open(FILENAME, "r")
    f.readline()  # skip header

    line = f.readline()
    while line:
        parts = line.strip().split(",")
        if len(parts) >= 5:
            print(
                "INV #", parts[0],
                "| Client", parts[1],
                "| $", parts[2],
                "|", parts[3],
                "|", parts[4]
            )
        line = f.readline()

    f.close()


# --- PROGRAM START ---
init_file()

while True:
    print("\n" + "!"*25)
    print("   INVOICE TRACKER")
    print("!"*25)
    print("1. Create New Invoice")
    print("2. List All Invoices")
    print("3. Exit Tracker")

    choice = input("Selection: ")

    if choice == "1":
        print("\nEnter invoice details:")
        client_id = input("Client ID: ")
        amount = input("Amount: ")
        date = input("Date (YYYY-MM-DD): ")
        desc = input("Description: ")

        new_id = get_next_id()
        data = (
            str(new_id) + "," +
            client_id + "," +
            amount + "," +
            date + "," +
            desc + "\n"
        )

        append_invoice(data)
        print("Invoice #" + str(new_id) + " saved successfully.")

    elif choice == "2":
        print("\n--- INVOICE HISTORY ---")
        display_invoices()
        print("-----------------------")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Try again.")

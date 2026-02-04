FILENAME = "expenses.txt"

# --- FUNCTIONS ---
def init_file():
    try:
        f = open(FILENAME, "r")
        f.close()
    except:
        print("Creating expense database...")
        f = open(FILENAME, "w")
        f.write("id,category,amount,date,description\n")
        f.close()


def read_all_lines():
    f = open(FILENAME, "r")
    lines = f.readlines()
    f.close()
    return lines


def get_next_id():
    lines = read_all_lines()
    return len(lines)


def append_expense(data_line):
    f = open(FILENAME, "a")
    f.write(data_line)
    f.close()


def display_expenses():
    f = open(FILENAME, "r")
    f.readline()  # skip header

    line = f.readline()
    while line:
        data = line.strip().split(",")

        if len(data) >= 5:
            eid = data[0]
            cat = data[1]
            val = data[2]
            dt = data[3]
            ds = data[4]

            print("ID:", eid, "|", dt, "|", cat, "| $", val, "|", ds)

        line = f.readline()

    f.close()


# --- PROGRAM START ---
init_file()

while True:
    print("\n" + "-"*30)
    print("      EXPENSE TRACKER")
    print("-"*30)
    print("1. Record a New Expense")
    print("2. View All Expenses")
    print("3. Return to Main OS")

    choice = input("Option: ")

    if choice == "1":
        print("\nEntering expense data:")
        category = input("Category: ")
        amount = input("Amount: ")
        date = input("Date (YYYY-MM-DD): ")
        desc = input("Description: ")

        entry_id = get_next_id()

        data_line = (
            str(entry_id) + "," +
            category + "," +
            amount + "," +
            date + "," +
            desc + "\n"
        )

        append_expense(data_line)
        print("SAVED: '" + category + "' expense recorded.")

    elif choice == "2":
        print("\n--- RECORDED EXPENSES ---")
        display_expenses()
        print("-" * 30)

    elif choice == "3":
        print("Closing Expense Tracker...")
        break

    else:
        print("Error: Input 1, 2, or 3.")

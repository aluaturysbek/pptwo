from connect import connect
import csv

# -------- INSERT FROM CONSOLE --------
def insert_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


# -------- INSERT FROM CSV --------
def insert_from_csv(file):
    conn = connect()
    cur = conn.cursor()

    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (first_name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()


# -------- SEARCH --------
def search_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE first_name ILIKE %s",
        (f"%{name}%",)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


# -------- UPDATE --------
def update_contact(old_name, new_name=None, new_phone=None):
    conn = connect()
    cur = conn.cursor()

    if new_name:
        cur.execute(
            "UPDATE contacts SET first_name=%s WHERE first_name=%s",
            (new_name, old_name)
        )

    if new_phone:
        cur.execute(
            "UPDATE contacts SET phone=%s WHERE first_name=%s",
            (new_phone, old_name)
        )

    conn.commit()
    cur.close()
    conn.close()


# -------- DELETE --------
def delete_contact(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE first_name=%s OR phone=%s",
        (value, value)
    )

    conn.commit()
    cur.close()
    conn.close()


# -------- MENU --------
while True:
    print("\n1.Insert console")
    print("2.Insert CSV")
    print("3.Search")
    print("4.Update")
    print("5.Delete")
    print("0.Exit")

    choice = input("Choose: ")

    if choice == "1":
        insert_console()

    elif choice == "2":
        insert_from_csv("contacts.csv")

    elif choice == "3":
        search_by_name(input("Name: "))

    elif choice == "4":
        update_contact(
            input("Old name: "),
            input("New name (or press Enter): "),
            input("New phone (or press Enter): ")
        )

    elif choice == "5":
        delete_contact(input("Enter name or phone: "))

    elif choice == "0":
        break
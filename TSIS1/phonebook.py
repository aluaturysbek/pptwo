import json
from connect import connect

# ---------------- SEARCH ----------------
def search():
    conn = connect()
    cur = conn.cursor()

    q = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    print(cur.fetchall())

    conn.close()


# ---------------- PAGINATION ----------------
def paginate():
    conn = connect()
    cur = conn.cursor()

    limit = 3
    offset = 0

    while True:
        cur.execute("SELECT * FROM get_contacts_paginated(%s,%s)", (limit, offset))
        print(cur.fetchall())

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev" and offset > 0:
            offset -= limit
        else:
            break

    conn.close()


# ---------------- ADD PHONE ----------------
def add_phone():
    conn = connect()
    cur = conn.cursor()

    name = input("Contact name: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, ptype))
    conn.commit()

    conn.close()


# ---------------- MOVE GROUP ----------------
def move_group():
    conn = connect()
    cur = conn.cursor()

    name = input("Contact name: ")
    group = input("Group: ")

    cur.execute("CALL move_to_group(%s,%s)", (name, group))
    conn.commit()

    conn.close()


# ---------------- EXPORT JSON ----------------
def export_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """)

    data = cur.fetchall()

    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(data, f, default=str)

    print("Export done")
    conn.close()


# ---------------- IMPORT JSON ----------------
def import_json():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for row in data:
        name = row[0]

        cur.execute("SELECT 1 FROM contacts WHERE name=%s", (name,))
        if cur.fetchone():
            if input(f"{name} exists. overwrite? (y/n): ") != "y":
                continue
            cur.execute("DELETE FROM contacts WHERE name=%s", (name,))

        cur.execute(
            "INSERT INTO contacts(name,email,birthday) VALUES(%s,%s,%s)",
            (row[0], row[1], row[2])
        )

    conn.commit()
    conn.close()


# ---------------- MENU ----------------
while True:
    print("\n1.Search")
    print("2.Pagination")
    print("3.Add phone")
    print("4.Move group")
    print("5.Export JSON")
    print("6.Import JSON")
    print("0.Exit")

    choice = input("Choose: ")

    if choice == "1":
        search()
    elif choice == "2":
        paginate()
    elif choice == "3":
        add_phone()
    elif choice == "4":
        move_group()
    elif choice == "5":
        export_json()
    elif choice == "6":
        import_json()
    elif choice == "0":
        break
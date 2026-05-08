from connect import conn

cur = conn.cursor()


def call_upsert(name, phone):
    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))


def search_contacts(text):
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s);", (text,))
    return cur.fetchall()


def get_paginated(limit, offset):
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
    return cur.fetchall()


def delete_contact(value):
    cur.execute("CALL delete_contact(%s);", (value,))


def insert_many(names, phones):
    cur.execute("CALL insert_many_contacts(%s, %s);", (names, phones))


# Example usage
if __name__ == "__main__":
    call_upsert("Ali", "77001234567")

    print(search_contacts("Ali"))

    print(get_paginated(5, 0))

    delete_contact("Ali")

    insert_many(
        ["John", "Mike", "Sara"],
        ["1234567", "invalid_phone", "+77005554433"]
    )
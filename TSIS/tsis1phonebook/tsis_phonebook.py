import psycopg2
import json
import csv
import os
from new_connect import connect_to_db

conn = connect_to_db()
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS groups (id SERIAL PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL);
    CREATE TABLE IF NOT EXISTS better_phonebook (
        id SERIAL PRIMARY KEY, name VARCHAR(100) UNIQUE, phonenumber VARCHAR(50),
        email VARCHAR(100), birthday DATE, group_id INTEGER REFERENCES groups(id)
    );
    CREATE TABLE IF NOT EXISTS phones (
        id SERIAL PRIMARY KEY, contact_id INTEGER REFERENCES better_phonebook(id) ON DELETE CASCADE,
        phone VARCHAR(20) NOT NULL, type VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile'))
    );
""")
conn.commit()

def menu():
    while True:
        print("\n--- Better Phonebook ---")
        print("1. Add a contact")
        print("2. Delete a contact")
        print("3. Add multiple contacts")
        print("4. Get contacts by a pattern")
        print("5. Pagination (Interactive)")
        print("6. Advanced Filter & Sort")
        print("7. Import/Export (JSON/CSV)")
        print("8. Add secondary phone")
        print("9. Move contact to group")
        print("10. Quit")

        choose = input("What would you like to do? : ")

        if choose == '1':
            namee = input("Write a name: ")
            numberr = input("Write a phone number: ")
            cursor.execute("CALL upsert_contact(%s, %s)", (namee, numberr))
            conn.commit()

        elif choose == "2":
            term = input("Write an info (name or phone): ")
            cursor.execute("CALL delete_contact(%s)", (term,))
            conn.commit()

        elif choose == "3":
            names = input("Write names (space separated): ").split()
            numbers = input("Write phone numbers (space separated): ").split()
            cursor.execute("CALL bulk_insert(%s, %s, %s)", (names, numbers, []))
            errors = cursor.fetchone()[0]
            if errors: print("Errors:", errors)
            else: print("All contacts added successfully!")
            conn.commit()

        elif choose == "4":
            pattern = input("Write a pattern (name, email, or ANY phone): ")
            cursor.execute("SELECT * FROM search_contacts(%s)", (pattern,))
            inf = cursor.fetchall()
            for row in inf: print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}")
            conn.commit()

        elif choose == "5": 
            limit = int(input("Write a limit per page: "))
            offset = 0
            while True:
                cursor.execute("SELECT * FROM pagination(%s, %s)", (limit, offset))
                info = cursor.fetchall()
                print("\n--- Page ---")
                if not info: print("No more contacts.")
                else:
                    for i in info: print(f"{i[1]} - {i[2]}")
                
                nav = input("\n[n] Next page, [p] Prev page, [q] Quit pagination: ").strip().lower()
                if nav == 'n': offset += limit
                elif nav == 'p': offset = max(0, offset - limit)
                elif nav == 'q': break
            conn.commit()

        elif choose == "6": 
            print("a. Filter by Group | b. Search by Email | c. Sort Results")
            sub = input("Choose: ")
            if sub == 'a':
                grp = input("Group name: ")
                cursor.execute("SELECT b.name FROM better_phonebook b JOIN groups g ON b.group_id = g.id WHERE g.name = %s", (grp,))
                for row in cursor.fetchall(): print(row[0])
            elif sub == 'b':
                mail = input("Email pattern: ")
                cursor.execute("SELECT name, email FROM better_phonebook WHERE email ILIKE %s", ('%' + mail + '%',))
                for row in cursor.fetchall(): print(f"{row[0]} - {row[1]}")
            elif sub == 'c':
                sort_by = input("Sort by (name / birthday / date): ")
                if sort_by == 'name': cursor.execute("SELECT name, birthday FROM better_phonebook ORDER BY name")
                elif sort_by == 'birthday': cursor.execute("SELECT name, birthday FROM better_phonebook ORDER BY birthday")
                else: cursor.execute("SELECT name, id FROM better_phonebook ORDER BY id DESC") 
                for row in cursor.fetchall(): print(row)

        elif choose == "7": 
            print("a. Export JSON | b. Import JSON | c. Import CSV")
            sub = input("Choose: ")
            if sub == 'a':
                cursor.execute("SELECT name, phonenumber, email FROM better_phonebook")
                data = [{"name": r[0], "phone": r[1], "email": r[2]} for r in cursor.fetchall()]
                with open("contacts.json", "w") as f: json.dump(data, f)
                print("Exported to contacts.json")
            elif sub == 'b':
                if os.path.exists("contacts.json"):
                    with open("contacts.json", "r") as f:
                        data = json.load(f)
                        for item in data:
                            cursor.execute("SELECT 1 FROM better_phonebook WHERE name = %s", (item['name'],))
                            if cursor.fetchone():
                                act = input(f"Contact {item['name']} exists. (s)kip or (o)verwrite? ")
                                if act == 'o':
                                    cursor.execute("UPDATE better_phonebook SET phonenumber=%s, email=%s WHERE name=%s", (item['phone'], item['email'], item['name']))
                            else:
                                cursor.execute("INSERT INTO better_phonebook(name, phonenumber, email) VALUES(%s, %s, %s)", (item['name'], item['phone'], item.get('email')))
                    conn.commit()
                    print("JSON imported!")
            elif sub == 'c':
                filename = input("CSV filename (e.g., contacts.csv): ")
                if os.path.exists(filename):
                    with open(filename, "r") as f:
                        reader = csv.reader(f)
                        for row in reader:

                            if len(row) >= 2:
                                cursor.execute("INSERT INTO better_phonebook(name, phonenumber) VALUES(%s, %s) ON CONFLICT (name) DO NOTHING", (row[0], row[1]))
                    conn.commit()
                    print("CSV imported!")

        elif choose == "8":
            name = input("Contact Name: ")
            phone = input("New Phone: ")
            ptype = input("Type (home/work/mobile): ")
            cursor.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
            conn.commit()
            print("Phone added!")

        elif choose == "9":
            name = input("Contact Name: ")
            grp = input("Group Name (Family, Work, etc): ")
            cursor.execute("CALL move_to_group(%s, %s)", (name, grp))
            conn.commit()
            print("Moved to group!")

        elif choose == '10':
            print("Programme is closed. Byeee")
            break

menu()

cursor.close()
conn.close()
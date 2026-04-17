import psycopg2
from new_connect import connect_to_db

conn = connect_to_db()
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS better_phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phonenumber VARCHAR(50)
        )
    """)
conn.commit()



def menu():
    while True:
        print("better phonebook")
        print("1.Add a contact")
        print("2.Delete a contact")
        print("3.Add multiple contacts")
        print("4.Get contacts by a pattern")
        print("5.Pagination")
        print("6.Quit")

        choose = input("What would you like to do? : ")

        if choose == '1': #adding
            namee = input("Write a name: ")
            numberr = input("Write a phone number: ")
            cursor.execute("CALL upsert_contact(%s, %s)", (namee, numberr))
            conn.commit()
        
        elif choose == "2": #deleting
            term = input("Write an info: ")
            cursor.execute("CALL delete_contact(%s)", (term,))
            conn.commit()

        elif choose == "3": #adding multiple
            names = input("Write names: ").split()
            numbers = input("write phone numbers: ").split()
            cursor.execute("CALL bulk_insert(%s, %s, %s)", (names, numbers, []))
            inf = cursor.fetchone()
            errors = inf[0]
            if errors:
                print("Not added contacts due to error in name and/or phone number: ")
                print(errors)
            else:
                print("All contacts added successfully!")
            conn.commit()

        elif choose == "4": #get by pattern
            pattern = input("Write a pattern: ")
            cursor.execute("SELECT * FROM get_contacts_by_pattern(%s)",(pattern,))
            inf = cursor.fetchall()
            if not inf:
                print("No contacts found")
            else:
                for row in inf:
                    print(f"\nname: {row[1]}\nphone numebr: {row[2]}\n")
            conn.commit()

        elif choose == "5": #pagination
            limit = int(input("Write a limit: "))
            offset = int(input("Write an offset: "))
            cursor.execute("SELECT * FROM pagination(%s, %s)", (limit, offset))
            info = cursor.fetchall()
            if not info:
                print("No contacts!")
            else:
                for i in info:
                    print(f"\nname: {i[1]}\nphone numebr: {i[2]}\n")
            conn.commit()

        elif choose == '6':
            print("Programme is closed. byeee")
            break

menu()

cursor.close()
conn.close()

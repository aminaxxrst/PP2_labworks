import csv
from connect import connect

def menu():
    while True:
        print("\n===== PRACTICE 8: PHONEBOOK (SQL FUNCTIONS) =====")
        print("1. Add/Update Contact (Upsert)")
        print("2. Search Contacts (Pattern)")
        print("3. Paginated View")
        print("4. Bulk Insert from CSV (with Validation)")
        print("5. Delete Contact (by Name or Phone)")
        print("6. Exit")
        
        choice = input("Option choose: ")

        # 1. Қосу немесе жаңарту
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            
            conn = connect()
            cur = conn.cursor()
            cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
            conn.commit()
            cur.close()
            conn.close()
            print("Done!")

        # 2. Үлгі бойынша іздеу
        elif choice == "2":
            pattern = input("Enter name or phone part: ")
            
            conn = connect()
            cur = conn.cursor()
            cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
            rows = cur.fetchall()
            cur.close()
            conn.close()
            
            print("\nSearch Results:")
            for row in rows:
                print(f"Name: {row[0]} | Phone: {row[1]}")

        # 3. Пагинация (бөліп көрсету)
        elif choice == "3":
            limit = int(input("How many rows to show? "))
            offset = int(input("How many rows to skip (offset)? "))
            
            conn = connect()
            cur = conn.cursor()
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            rows = cur.fetchall()
            cur.close()
            conn.close()
            
            print("\nPaginated View:")
            for row in rows:
                print(f"Name: {row[0]} | Phone: {row[1]}")

        # 4. CSV-ден жаппай қосу (Валидациямен)
        elif choice == "4":
            names = []
            phones = []
            with open("contact.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    names.append(row[0])
                    phones.append(row[1])
            
            conn = connect()
            cur = conn.cursor()
            # CALL кезінде үшінші параметр (OUT) үшін NULL береміз
            cur.execute("CALL insert_many_contacts(%s, %s, NULL)", (names, phones))
            invalid_entries = cur.fetchone()
            conn.commit()
            cur.close()
            conn.close()
            print(f"Import finished. Invalid entries found: {invalid_entries}")

        # 5. Өшіру
        elif choice == "5":
            val = input("Enter name or phone to delete: ")
            
            conn = connect()
            cur = conn.cursor()
            cur.execute("CALL delete_contact(%s)", (val,))
            conn.commit()
            cur.close()
            conn.close()
            print("Action completed.")

        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
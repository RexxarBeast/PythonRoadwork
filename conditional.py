import sqlite3

connection = sqlite3.connect("sample.db")
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)"
)
connection.commit()
username = 'nando'
password = '123'

def logo():
    for attempt in range(5):
        try:
            user_input = input("enter your username ")
            pass_input = input("enter ur password ")
        except ValueError:
            print("invalid type of login")

        if user_input == username and pass_input == password:
            print("successfully login ")
            return True
        else:
            print(f"too many attempts{4-attempt}")
            return False
while True:
    if logo():
        print("welcome")
        break
    else:
        again = input("try again (y/n):")
        if again.lower() != 'y':
            print("gb")
            break

    
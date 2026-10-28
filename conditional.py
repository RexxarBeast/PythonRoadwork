import sqlite3

connection = sqlite3.connect("asdas.db")
cursor = connection.cursor()
# cursor.execute(
#     "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)"
# )
cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    ("nando", "123"),
)
connection.commit()

def logo():
    for attempt in range(5):
        try:
            user_input = input("enter your username ")
            pass_input = input("enter ur password ")
         
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
            user = cursor.fetchone()
        except ValueError:
            print("invalid type of login")

        if user:
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

    
import sqlite3

connection = sqlite3.connect("asdas.db")
cursor = connection.cursor()
# cursor.execute(
#     "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)"
# )
# cursor.execute(
#     "INSERT INTO users (username, password) VALUES (?, ?)",
#     ("nando", "123"),
# )
connection.commit()

def logo():
    for attempt in range(5):
      
        username = input("Enter your username: ")

        password = input("Enter your password: ")

        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        )
        user = cursor.fetchone()

        if user:
            print("Successfully logged in")
            return True

        remaining = 4 - attempt
        if remaining > 0:
            print(f"Wrong username or password. {remaining} attempts left.")

    print("Too many attempts.")
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

    
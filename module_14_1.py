import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
userneme TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email_index ON Users(email)")

# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (userneme, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}",
#                                                                                              f"exemple{i}@gmail.com",
#                                                                                              f"{i * 10}", 1000))

# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (i, ))



cursor.execute("SELECT  userneme, email, age FROM Users WHERE age != 60")
users = cursor.fetchall()

for user in users:
    print(user)

connection.commit()
connection.close()

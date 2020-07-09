import sqlite3
conn = sqlite3.connect('movie.db')
print("Opened database successfully")


cursor = conn.execute("SELECT id, title, year from MOVIE")
for row in cursor:
    print("ID = ", row[0])
    print("TITLE = ", row[1])
    print("YEAR = ", row[2], "\n")

print("Operation done successfully")
conn.close()

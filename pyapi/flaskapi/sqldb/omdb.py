import sqlite3
from services import get_movies


conn = sqlite3.connect('movie.db')
print("Opened database successfully")

#conn.execute('''CREATE TABLE MOVIE
#(ID INT PRIMARY KEY NOT NULL,
#TITLE TEXT NOT NULL,
#YEAR TEXT NOT NULL);''')

movies = get_movies()
i = 0
while i < len(movies):
    movie = movies[i]
    title = movie['Title']
    year = movie['Year']
    conn.execute(f"INSERT INTO MOVIE (ID, TITLE, YEAR) VALUES ({i}, '{title}', '{year}')")
    #print(f"INSERT INTO COMPANY (ID, TITLE, YEAR) VALUES ({i}, '{title}')")
    i +=1

conn.commit()

print("Table created successfully")
conn.close()

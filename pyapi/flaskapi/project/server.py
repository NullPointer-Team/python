from flask import Flask, render_template, request
from omdb import get_movies
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search_movie")
def new_student():
    return render_template("movie.html")

@app.route("/search_movie", methods=["POST", "GET"])
def search_movies():
    if request.method == "POST":
        try:
            title = request.form["title"]
            movies = get_movies(title)
            msg = "Successful Search"

        except:
            msg = "ERROR in Search"
            movies = []
        finally:
            return render_template("search_results.html", msg = msg, movies = movies)


@app.route("/addmovie", methods=["POST", "GET"])
def addmovie():
    i = 1
    if request.method == "POST":

        title = request.form["title"]
        year = request.form["year"]
        print(f"Title is {title}")
        print(f"Year is {year}")
        print(f"Counter is {i}")

        with sql.connect("movie.db") as conn:
            try:
                cur = conn.cursor()
                conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES
                        (ID TEXT NOT NULL,
                        TITLE TEXT NOT NULL,
                        YEAR TEXT NOT NULL);''')
                cur = conn.cursor()
                cur.execute(f"INSERT INTO movies (ID, TITLE, YEAR) VALUES (?,?,?)", (i, title, year))
                conn.commit()
                msg = "Record successfully added"
                i +=1
            except:
                msg = "ERROR in insert operations"
                conn.rollback()
            finally:
                return render_template("result.html", msg = msg)
                conn.close()


@app.route('/list')
def list():
    con = sql.connect("movie.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * from MOVIES")

    rows = cur.fetchall()
    return render_template("list.html", rows = rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

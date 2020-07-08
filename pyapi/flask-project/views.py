from flask import Flask, render_template, request, url_for, redirect, make_response, escape, session

app = Flask(__name__)
app.secret_key = "any random string"

@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        if request.method == "GET":
            return """
            Logged in as """ + username + """<br><b><a href = '/logout'>Click Here to Log Out</a></b>
            <form action = "" method = "post">
                <p><input type = text name = username></p>
                <p><input type = submit value = Login></p>
            </form>
          """
    return render_template("login.html")

@app.route("/username/<username>", methods = ["GET", "POST"])
def username(username):
    return render_template("user.html")


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for("index"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

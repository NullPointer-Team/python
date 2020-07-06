from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/login")
@app.route("/")
def index():
    return render_template("login.html")

@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST":
        if request.form.get("nm"):
            user = request.form.get("nm")
        else:
            user = "defaultuser"

        response = make_response(render_template("readcookie.html"))

        response.set_cookie("userID", user)

        return response

    if request.method == "GET":
        return redirect(url_for("index"))

@app.route("/getcookie")
def get_cookie():
    name = request.cookies.get("userID")

    return f'<h1>Welcome {name} </h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import session

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

app.secret_key = "632064767457"

@app.route("/")
def index():
    if "username" and "pwd" in session:
        return redirect(url_for("member")) 
    return render_template("welcome.html")

@app.route("/signin", methods=["POST"])
def signin():
    username=request.form["n"]
    pwd=request.form["p"]
    if username=="test" and pwd=="test":
        session["user"] = username
        session["pwd"] = pwd
        return redirect("member")
    elif (username == "") and (pwd == ""):
        return redirect(url_for("error", message="請輸入帳號、密碼"))
    else:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))

@app.route("/member")
def member():
    if "username" and "pwd" in session:
        return render_template("member.html")
    else:
        return redirect(url_for("index"))

@app.route("/error")
def error():
    data=request.args.get("message")
    return render_template("error.html", message=data)

@app.route("/signout")
def signout():
    session.pop("username", None)
    session.pop("pwd", None)
    return redirect(url_for("index"))

@app.route("/submit", methods=["POST"])
def submit():
        number = request.form["number"]
        return redirect(url_for("square", number=number))

@app.route("/square/<number>")
def square(number):
    return render_template("calculate.html", result = int(number) ** 2)

app.run(port=3000)
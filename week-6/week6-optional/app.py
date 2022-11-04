from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import session
from mysql.connector import connect


app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

app.secret_key = "632064767457"

mydb=connect(
    host="localhost",
    user="root",
    password="",
    database="website",
    charset = "utf8"  
)

@app.route("/")
def index():
    if "username" and "password" in session:
        return redirect(url_for("member")) 
    return render_template("welcome.html")

@app.route("/signup", methods=["POST"])
def signup():
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    with mydb.cursor() as cursor:
        cursor.execute("SELECT * FROM member WHERE username = %s", [username])
        cur = cursor.fetchone()
    if cur:
        return redirect(url_for("error", message="帳號已經被註冊"))
    elif (name == "") or (username == "") or (password == ""):
        return redirect(url_for("error", message="請輸入姓名、帳號或密碼"))
    else:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s);",[name, username, password])
            mydb.commit()
        return redirect(url_for("index"))

@app.route("/signin", methods=["POST"])
def signin():
    with mydb.cursor(dictionary=True) as cursor:
        username=request.form["username"]
        password=request.form["password"]
        cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s;", [username, password])
        cur = cursor.fetchone()
    if cur:
        session["name"]=cur["name"]
        session["username"]=cur["username"]
        session["password"]=cur["password"]
        return redirect("member")
    elif (username == "") and (password == ""):
        return redirect(url_for("error", message="請輸入帳號、密碼"))
    else:
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))

@app.route("/member")
def member():
    with mydb.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT member.name, message.content FROM member INNER JOIN message on member.id=message.member_id ORDER BY message.time DESC;")        
        cur = cursor.fetchall()
    if "username" and "password" in session:
        name=session["name"]
        return render_template("member.html",name=name,len = len(cur),cur=cur)
    else:
        return redirect(url_for("index"))

@app.route("/message", methods=["POST"])
def message():
    with mydb.cursor() as cursor:
        name=session["name"]
        cursor.execute("SELECT id FROM member where name= %s;",[name])
        member_id = (cursor.fetchone()[0])
        content=request.form["content"]
        cursor.execute("INSERT INTO message (member_id,content) VALUES (%s,%s);",[member_id,content])
        mydb.commit()
        return redirect(url_for("member"))

@app.route("/error")
def error():
    data=request.args.get("message")
    return render_template("error.html", message=data)

@app.route("/signout")
def signout():
    session.pop("username", None)
    session.pop("password", None)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(port=3000, debug=True)
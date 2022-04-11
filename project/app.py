from operator import methodcaller
from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

def db_conection():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    return cursor

@app.route("/", methods=["POST", "GET"])
def index():
    return redirect("/login")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        name = request.form.get("name")
        senha = request.form.get("senha")
        cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT, senha TEXT)")
        conn.commit()
        cursor.close()
        conn.close()
        return render_template("index.html")
    else:
        return render_template("login.html")


import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]
    cc = db.execute("SELECT cash FROM users WHERE id=?", user_id)
    cc =cc[0]
    lista = db.execute("SELECT * FROM cash WHERE user_id=?", user_id)
    return render_template("index.html", lista=lista, cc=cc)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    user_id = session["user_id"]
    transaction = "buy"
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        confere = lookup(symbol)
        if not shares.isdecimal():
            return apology("Please enter a valid input")
        shares = int(shares)
        if shares <= 0:
            return apology("Please enter a valid number")
        if confere == None or confere == []:
            return apology("Please enter a valid value")
        else:
            money = float(confere["price"])
        id = request.form.get("id")
        dinero = db.execute("SELECT cash FROM users WHERE id = ?", id)
        if dinero == [] or dinero == None or dinero == 0:
            return apology("No money")
        dinero = dinero[0]
        conta = dinero["cash"]

        if confere == [] or confere == None:
            return apology("This symbol doesn't exists",400)
        if confere:
            if conta < money*shares:
                return apology("No tienes dinero mi comprade")
            db.execute("INSERT INTO historico (user_id, shares, symbol, price, transactions) VALUES (?,?,?, ?,?)", id ,shares, symbol, confere["price"], transaction)
            dif = conta - (money*shares)
            shareANTES = db.execute("SELECT shares FROM cash WHERE user_id = ? AND symbol = ?", user_id, symbol)
            if shareANTES == [] or shareANTES == None:
                shareANTES =0
            else:
               shareANTES = shareANTES[0]
               shareANTES = shareANTES["shares"]
            shareFINAL = shareANTES+shares
            if not db.execute("SELECT user_id FROM cash WHERE user_id = ?", user_id):
                db.execute("INSERT INTO cash (user_id, shares, symbol, price) VALUES (?,?,?,?)", user_id, shareFINAL, symbol, money)
                db.execute("UPDATE users SET cash = ? WHERE id = ?", dif, user_id)
            if not db.execute("SELECT symbol FROM cash WHERE user_id = ? AND symbol = ?", user_id, symbol):
                db.execute("INSERT INTO cash (user_id, shares, symbol, price) VALUES (?,?,?,?)", user_id, shares, symbol, money)
                db.execute("UPDATE users SET cash = ? WHERE id = ?", dif, user_id)
            else:
                db.execute("UPDATE users SET cash = ? WHERE id = ?", dif, user_id)
                db.execute("UPDATE cash SET shares = ? WHERE user_id = ? AND symbol = ?", shareFINAL, user_id, symbol)
            return redirect("/")

    else:
        return render_template("buy.html", identificador = user_id)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    lista = db.execute("SELECT * FROM historico WHERE user_id=?", user_id)
    historico = db.execute("SELECT * FROM historico")
    return render_template("history.html", lista = lista)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/quote")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        symbol = symbol.upper()
        confere = lookup(symbol)
        if not confere:
            return apology("Please enter a valid symbol")
        else:
            return render_template("quoted.html", confere= confere)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        usersE = db.execute("SELECT * FROM users WHERE username = ?", username)
        if not username or not password or not confirmation:
            return apology("Please enter a valid input")
        if usersE:
            return apology("This username already exists")
        if password != confirmation:
            return apology("Please confirm your password")

        else:
            hashed = generate_password_hash(password, method='pbkdf2:sha256')
            db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hashed)
            return redirect("/login")
    if request.method == "GET":
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    user_id = session["user_id"]
    transaction = "sell"
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        id = request.form.get("id")
        pega = lookup(symbol)
        money = float(pega["price"])
        shares = int(shares)
        bag = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        bag = bag[0]
        bag = bag["cash"]
        amont = money*shares
        final = bag + (money*shares)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", final, user_id)
        parcelas = db.execute("SELECT SUM(shares) FROM cash WHERE user_id = ? AND symbol = ?", user_id, symbol)
        sharesF = db.execute("SELECT shares FROM cash WHERE user_id = ? AND symbol=?", user_id, symbol)
        sharesF = sharesF[0]
        sharesF = sharesF["shares"]
        parcelas = parcelas[0]
        parcelas = parcelas["SUM(shares)"]
        if parcelas == None:
            return apology("You don't have any shares of this stock")
        if bag < amont:
            return apology("You don't have enough money for thos shares/stocks")
        if sharesF < shares:
            return apology("You don't have those amont of shares of this stock")
        total = parcelas - shares
        db.execute("UPDATE cash SET shares = ? WHERE user_id = ? AND symbol = ?", total, user_id, symbol)
        db.execute("INSERT INTO historico (user_id, shares, symbol, price, transactions) VALUES (?,?,?, ?,?)", user_id, shares, symbol, money, transaction)
        return redirect("/")
    return render_template("sell.html", identificador=user_id)

@app.route("/add", methods=["POST", "GET"])
@login_required
def add():
    user_id = session["user_id"]
    if request.method == "POST":
        amount = request.form.get("amount")
        dinero = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        amount = float(amount)
        if amount<0:
            return apology("Please enter a valid value")
        else:
            if dinero == []:
                dinero = 0
            dinero = dinero[0]
            dinero = dinero["cash"]
            total = dinero + amount
            db.execute("UPDATE users SET cash = ? WHERE id = ?", total, user_id)
            return redirect("/")
    return render_template("add.html")

from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Soccer",
    "daniel silva"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/home", methods=["POST"])
def home():
    nome = request.form.get("gta5")
    if not request.form.get("gta5") or request.form.get("sport") not in SPORTS:
        return render_template("fail.html")
    else:
        return render_template("home.html", name = nome)
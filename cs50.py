from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL

# Remember to close the connection
#conn.close()
# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///property.db")
# variable = db.execute("[SQL Commands]")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("homepage.html")

@app.route("/payment", methods=["GET", "POST"])
def payment():
    if request.method == "GET":
        return render_template("payment.html")
    
@app.route("/properties", methods=["GET", "POST"])
def properties():
    if request.method == 'GET':
        return render_template("properties.html")
    
@app.route("/forsale", methods=["GET", "POST"])
def forsale():
    if request.method == 'GET':
        six_houses = [7, 8, 9, 10, 11, 12]
        return render_template("forsale.html", houses=six_houses)
    
@app.route("/forrent", methods=["GET", "POST"])
def forrent():
    if request.method == 'GET':
        return render_template("forrent.html")

    
if __name__ == "__main__":
    app.run(debug=True)

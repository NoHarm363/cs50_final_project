from flask import Flask, flash, redirect, render_template, request, session, g
from flask_session import Session
from cs50 import SQL
import json
import os

# Remember to close the connection
#conn.close()
# Configure application
app = Flask(__name__)

DATABASE = 'property.db'

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///property.db")
query = db.execute("SELECT * FROM users")

#for users table in our database, 0 = default users, 1 = admin

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        indexPropertyList = []
        #print('INDEX ROLE: ',session['admin'])
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            return render_template("homepage.html", houses=indexPropertyDict)

@app.route("/payment", methods=["GET", "POST"])
def payment():
    if request.method == "GET":
        return render_template("payment.html")

#parameter after the second /
@app.route("/propDetail/", methods=["GET", "POST"])
def propDet():
    if request.method == "GET":
        return render_template("propDet.html")
        
@app.route("/forsale", methods=["GET", "POST"])
def forsale():
    if request.method == 'GET':
        six_houses = [7, 8, 9, 10, 11, 12]
        return render_template("forsale.html", houses=six_houses)
    
@app.route("/forrent", methods=["GET", "POST"])
def forrent():
    if request.method == 'GET':
        return render_template("forrent.html")
    
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == 'GET':
        return render_template("admin.html")

@app.route("/admin/add_property", methods=["GET", "POST"])
def add_property():
    indexPropertyList = []
    if request.method == 'GET':
        return render_template("add_property.html")
    if request.method == 'POST':
        file_path = 'index_property.txt'
        if os.path.exists(file_path):
            with open("index_property.txt", "r") as file:
                index_property = file.read()
                jsonDict = json.loads(index_property)
                name = request.form.get("property_name")
                img = request.form.get("property_img_url")
                img = str(img)
                indexJson = json_add_property(name, img)
                for eachDict in jsonDict:
                    indexPropertyList.append(eachDict)
                indexPropertyList.append(indexJson)

        else:
            name = request.form.get("property_name")
            img = request.form.get("property_img_url")
            img = str(img)
            indexJson = json_add_property(name, img)
            indexPropertyList.append(indexJson)

        with open("index_property.txt", "w") as file:
            indexPropertyList = json.dumps(indexPropertyList)
            file.write(indexPropertyList)
        return redirect("/admin/add_property")


@app.route("/login", methods=["GET","POST"])
def login():
    # Query database for username
    #rows = db.execute(
    #"SELECT * FROM users WHERE username = ?", request.form.get("username")
    #)
    # Remember which user has logged in
    #session["user_id"] = rows[0]["id"]
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        query = db.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';")

        if len(query) == 1:
            print(query)
            session["username"] = username
            session["admin"] = admin 
            return render_template('login.html')
        
        else:
            return render_template('login.html')


        
       
if __name__ == "__main__":
    app.run(debug=True)

def json_add_property(name, img):
    jsonDict = {"property_name" : name, "img_url" : img}
    #jsonPropertyDict = json.dumps(jsonDict)
    return jsonDict

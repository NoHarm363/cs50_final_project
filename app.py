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
            print(indexPropertyDict)
            return render_template("homepage.html", houses=indexPropertyDict)

@app.route("/payment", methods=["GET", "POST"])
def payment():
    if request.method == "GET":
        return render_template("payment.html")

#parameter after the second /
@app.route("/propDescription", methods=["GET", "POST"])
def propDescription():
    if request.method == "GET":
        return render_template("prop_desc.html")
    
#parameter after the second /
@app.route("/propDetail/", methods=["GET", "POST"])
def propDet():
    if request.method == "GET":
        return render_template("propDet.html")
        
@app.route("/forsale", methods=["GET", "POST"])
def forsale():
    if request.method == 'GET':
        for_sale = "For Sale"
        for_sale_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if for_sale in property["sale_status"]:
                    for_sale_list.append(property)
            return render_template("forsale.html", for_sale_houses=for_sale_list)
    
@app.route("/forrent", methods=["GET", "POST"])
def forrent():
    if request.method == 'GET':
        for_rent = "For Rent"
        for_rent_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if for_rent in property["sale_status"]:
                    for_rent_list.append(property)
            return render_template("forrent.html", for_rent_houses=for_rent_list)

@app.route("/condo", methods=["GET", "POST"])
def condo():
    if request.method == 'GET':
        condo = "Condo"
        condo_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if condo in property["sale_status"]:
                    condo_list.append(property)
            return render_template("condo.html", condo_houses=condo_list)

@app.route("/mortgages", methods=["GET", "POST"])
def mortgages():
    if request.method == 'GET':
        mortgage = "Mortgage"
        mortgage_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if mortgage in property["sale_status"]:
                    mortgage_list.append(property)
            return render_template("mortgage.html", mortgage_houses=mortgage_list)

@app.route("/commercial", methods=["GET", "POST"])
def commercial():
    if request.method == 'GET':
        commercial = "Commercial"
        commercial_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if commercial in property["sale_status"]:
                    commercial_list.append(property)
            return render_template("commercial.html", commercial_houses=commercial_list)

@app.route("/bungalow_villa", methods=["GET", "POST"])
def bungalow_villa():
    if request.method == 'GET':
        bungalow_villa = "Bungalow/Villa"
        bungalow_villa_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if bungalow_villa in property["sale_status"]:
                    bungalow_villa_list.append(property)
            return render_template("bungalow_villa.html", bungalow_villa_houses=bungalow_villa_list)

@app.route("/apartment_condo_service", methods=["GET", "POST"])
def apartment_condo_service():
    if request.method == 'GET':
        apartment_condo_service = 'Apartment/Condo/Service'
        apartment_condo_service_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if apartment_condo_service in property["sale_status"]:
                    apartment_condo_service_list.append(property)
            return render_template("apartment_condo_service.html", apartment_condo_service_houses=apartment_condo_service_list)

@app.route("/semi_detached_house", methods=["GET", "POST"])
def semi_detached_house():
    if request.method == 'GET':
        semi_detached_house = 'Semi-Detached House'
        semi_detached_house_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if semi_detached_house in property["sale_status"]:
                    semi_detached_house_list.append(property)
            return render_template("semi_detached_house.html", semi_detached_house_houses=semi_detached_house_list)

@app.route("/terrace_link_house", methods=["GET", "POST"])
def terrace_link_house():
    if request.method == 'GET':
        terrace_link_house = 'Semi-Detached House'
        terrace_link_house_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if terrace_link_house in property["sale_status"]:
                    terrace_link_house_list.append(property)
            return render_template("terrace_link_house.html", terrace_link_house_houses=terrace_link_house_list)

@app.route("/industrial", methods=["GET", "POST"])
def industrial():
    if request.method == 'GET':
        industrial = 'Industrial'
        industrial_house_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if industrial in property["sale_status"]:
                    industrial_house_list.append(property)
            return render_template("industrial.html", industrial_houses=industrial_house_list)
        
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == 'GET':
        return render_template("admin.html")

@app.route("/admin/add_property", methods=["GET", "POST"])
def add_property():
    indexPropertyList = []
    if request.method == 'GET':
        PropertyTypeList = ['Bungalow/Villa', 'Apartment/Condo/Service', 'Semi-Detached House', 'Terrace/Link House', 'Commercial', 'Industrial', 'Agriculture Land', 'Others']
        SaleStatusList = ['For Sale', 'For Rent', 'Condo', 'Mortgage', 'Commercial']
        return render_template("add_property.html", propertyType=PropertyTypeList, saleStatus=SaleStatusList)
    if request.method == 'POST':
        file_path = 'index_property.txt'
        if os.path.exists(file_path):
            with open("index_property.txt", "r") as file:
                index_property = file.read()
                jsonDict = json.loads(index_property)
                name = request.form.get("property_name")
                img = request.form.get("property_img_url")
                img = str(img)
                property_type = request.form.get("PropertyType")
                sale_status = request.form.getlist("SaleStatus")
                indexJson = json_add_property(name, img, property_type, sale_status)
                for eachDict in jsonDict:
                    indexPropertyList.append(eachDict)
                indexPropertyList.append(indexJson)

        else:
            name = request.form.get("property_name")
            img = request.form.get("property_img_url")
            img = str(img)
            property_type = request.form.get("PropertyType")
            sale_status = request.form.getlist("SaleStatus")
            indexJson = json_add_property(name, img, property_type, sale_status)
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

def json_add_property(name, img, property_type, sale_status):
    jsonDict = {"property_name" : name, "img_url" : img, "property_type" : property_type, "sale_status" : sale_status}
    #jsonPropertyDict = json.dumps(jsonDict)
    return jsonDict

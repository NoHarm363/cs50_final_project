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

#Saved upload property photos in a directory
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#for users table in our database, 0 = default users, 1 = admin

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        #print('INDEX ROLE: ',session['admin'])
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            return render_template("homepage.html", houses=indexPropertyDict)

@app.route("/payment", methods=["GET", "POST"])
def payment():
    if request.method == "GET":
        return render_template("payment.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")

@app.route("/propDetailBeta", methods=["GET", "POST"])
def propDetBeta():
        if request.method == "GET":
            with open("index_property.txt", "r") as file:
                index_property = file.read()
                indexPropertyDict = json.loads(index_property)
            with open("agent.txt", "r") as file:
                agent_txt = file.read()
                agentDict = json.loads(agent_txt)
            return render_template("prop_desc.html", houses=indexPropertyDict, responsible_agents=agentDict)

#parameter after the second /
@app.route("/propDetail/", methods=["GET", "POST"])
def propDet():
    if request.method == "GET":
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
        with open("agent.txt", "r") as file:
            agent_txt = file.read()
            agentDict = json.loads(agent_txt)
        property_name = request.args.get("name")
        return render_template("prop_desc_template.html", houses=indexPropertyDict, responsible_agents=agentDict, property_name=property_name)
    
    #handle if not normal user
    if request.method == 'POST':
        file_path = 'carts.txt'

        if os.path.exists(file_path):
            with open(file_path, "a") as file:
                carts = {}
                if session['username'] not in carts:
                    carts[session['username']] = []
                carts[session['username']].append('house details')
                print(carts)
                file.write(json.dumps(carts))
        
        #add property to cart which will finally be booked 
        #together with other properties that are in the cart.

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
                if bungalow_villa in property["property_type"]:
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
                if apartment_condo_service in property["property_type"]:
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
                if semi_detached_house in property["property_type"]:
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
                if terrace_link_house in property["property_type"]:
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
                if industrial in property["property_type"]:
                    industrial_house_list.append(property)
            return render_template("industrial.html", industrial_houses=industrial_house_list)

@app.route("/agriculture_land", methods=["GET", "POST"])
def agriculture_land():
    if request.method == 'GET':
        agriculture_land = 'Agriculture Land'
        agriculture_land_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if agriculture_land in property["property_type"]:
                    agriculture_land_list.append(property)
            return render_template("agriculture_land.html", agriculture_lands=agriculture_land_list)
        
@app.route("/others", methods=["GET", "POST"])
def others():
    if request.method == 'GET':
        others = 'Others'
        others_list = []
        with open("index_property.txt", "r") as file:
            index_property = file.read()
            indexPropertyDict = json.loads(index_property)
            for property in indexPropertyDict:
                if others in property["property_type"]:
                    others_list.append(property)
            return render_template("others.html", others=others_list)


@app.route("/overview", methods=["GET", "POST"])
def overview():
    if request.method == 'GET':
        # Read the JSON file
        with open("agent.txt", "r") as file:
            content = file.read()  # Read the file content as a string
        # Parse the JSON string into a Python object
        agents = json.loads(content)
        return render_template("overview_template.html", agents=agents)

@app.route("/overview/nevada_agent", methods=["GET", "POST"])
def nevada():
    agent_list = []
    if request.method == 'GET':
        with open("agent.txt", "r") as file:
            content = file.read()  # Read the file content as a string
        # Parse the JSON string into a Python object
            agents = json.loads(content)
        for agent in agents:
            if 'Nevada' in agent['agent_work_states']:
                agent_list.append(agent)
        return render_template("overview_template.html", agents=agent_list)

@app.route("/overview/chicago_agent", methods=["GET", "POST"])
def chicago():
    agent_list = []
    if request.method == 'GET':
        with open("agent.txt", "r") as file:
            content = file.read()  # Read the file content as a string
        # Parse the JSON string into a Python object
            agents = json.loads(content)
        for agent in agents:
            if "Chicago" in agent['agent_work_states']:
                agent_list.append(agent)
        return render_template("overview_template.html", agents=agent_list)

@app.route("/overview/texas_agent", methods=["GET", "POST"])
def texas():
    agent_list = []
    if request.method == 'GET':
        with open("agent.txt", "r") as file:
            content = file.read()  # Read the file content as a string
        # Parse the JSON string into a Python object
            agents = json.loads(content)
        for agent in agents:
            if "Texas" in agent['agent_work_states']:
                agent_list.append(agent)
        return render_template("overview_template.html", agents=agent_list)
    
@app.route("/overview/washington_agent", methods=["GET", "POST"])
def washington():
    agent_list = []
    if request.method == 'GET':
        with open("agent.txt", "r") as file:
            content = file.read()  # Read the file content as a string
        # Parse the JSON string into a Python object
            agents = json.loads(content)
        for agent in agents:
            if "Washington DC" in agent['agent_work_states']:
                agent_list.append(agent)
        return render_template("overview_template.html", agents=agent_list)

@app.route("/overview/los_angeles_agent", methods=["GET", "POST"])
def los_angeles():
    agent_list = []
    if request.method == 'GET':
        with open("agent.txt", "r") as file:
            content = file.read()  # Read the file content as a string
        # Parse the JSON string into a Python object
            agents = json.loads(content)
        for agent in agents:
            if "Los Angeles" in agent['agent_work_states']:
                agent_list.append(agent)
        return render_template("overview_template.html", agents=agent_list)

@app.route("/overview/california_agent", methods=["GET", "POST"])
def california():
    agent_list = []
    if request.method == 'GET':
        with open("agent.txt", "r") as file:
            content = file.read()  # Read the file content as a string
        # Parse the JSON string into a Python object
            agents = json.loads(content)
        for agent in agents:
            if "California" in agent['agent_work_states']:
                agent_list.append(agent)
        return render_template("overview_template.html", agents=agent_list)

@app.route("/overview/san_francisco_agent", methods=["GET", "POST"])
def san_francisco():
    agent_list = []
    if request.method == 'GET':
        with open("agent.txt", "r") as file:
            content = file.read()  # Read the file content as a string
        # Parse the JSON string into a Python object
            agents = json.loads(content)
        for agent in agents:
            if "San Francisco" in agent['agent_work_states']:
                agent_list.append(agent)
        return render_template("overview_template.html", agents=agent_list)

@app.route("/overview/new_jersey_agent", methods=["GET", "POST"])
def new_jersey():
    agent_list = []
    if request.method == 'GET':
        with open("agent.txt", "r") as file:
            content = file.read()  # Read the file content as a string
        # Parse the JSON string into a Python object
            agents = json.loads(content)
        for agent in agents:
            if "New Jersey" in agent['agent_work_states']:
                agent_list.append(agent)
        return render_template("overview_template.html", agents=agent_list)

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
        TenureTypeList = ['Freehold', 'Leasehold', 'Strate Title', 'Ground Lease']
        FacilitiesList = ['Swimming Pool', 'Gym', 'Playground', '24-Hour Security', 'Sport Facilities', 'Multi-purpose Halls', 'Sauna Room', 'Mini-Marts', 'Landscape Garden']
        LocationList = ["Nevada", "Chicago", "Texas", "Washington DC", "Los Angeles", "California", "San Franscisco", "New Jersey"]
        AgentList = ["Prinz Eugen", "CS50 Duck", "Frostleaf", "Texas", "Negev", "Eren Jeager", "Washington", "Nevada", "Chicago", "California", "New Jersey", "Enterprise"]
        return render_template("add_property.html", propertyType=PropertyTypeList, saleStatus=SaleStatusList, tenureType=TenureTypeList, facilities=FacilitiesList, locations=LocationList, responsible_agents=AgentList)
    
    if request.method == 'POST':
        file_path = 'index_property.txt'
        if os.path.exists(file_path):
            with open("index_property.txt", "r") as file:
                index_property = file.read()
                jsonDict = json.loads(index_property)
                name = request.form.get("property_name")
                print(f"All uploaded files: {request.files}")
                propDetImgs = request.files.getlist("PropDetImages")
                print(f"Files uploaded: {[img.filename for img in propDetImgs]}") 
                property_description = request.form.get("property_description")
                price = request.form.get("price")
                property_lot_size = request.form.get("lot_size")
                bedroom_number = request.form.get("bedroom_num")
                bathroom_number = request.form.get("bathroom_num")
                property_type = request.form.get("PropertyType")
                location = request.form.get("Property's Location")
                agent = request.form.get("ResponsibleAgent")
                sale_status = request.form.getlist("SaleStatus")
                tenure_type = request.form.getlist("TenureType")
                facilities = request.form.getlist("Facilities")
                #return saved and corrected pathway list of photos to this propDetImgsPaths variable
                propDetImgsPaths = SavedIMG(propDetImgs)
                print(f"Paths returned from SavedIMG: {propDetImgsPaths}")  # Debugging step
                if not propDetImgsPaths:
                    return "No images uploaded.", 400
                img = propDetImgsPaths[0]
                print(f"Main image: {img}")
                #img = "https://www.maramani.com/cdn/shop/files/4-bedrooommodernbungalowhouse-ID14511-Image01.jpg?v=1696423958&width=2048"
                indexJson = json_add_property(name, img, propDetImgsPaths, property_description, price, property_lot_size, bedroom_number, bathroom_number, property_type, location, agent, sale_status, tenure_type, facilities)
                for eachDict in jsonDict:
                    indexPropertyList.append(eachDict)
                indexPropertyList.append(indexJson)

        else:
                name = request.form.get("property_name")
                propDetImgs = request.files.getlist("PropDetImages")
                print(f"Files uploaded: {[img.filename for img in propDetImgs]}") 
                property_description = request.form.get("property_description")
                price = request.form.get("price")
                property_lot_size = request.form.get("lot_size")
                bedroom_number = request.form.get("bedroom_num")
                bathroom_number = request.form.get("bathroom_num")
                property_type = request.form.get("PropertyType")
                location = request.form.get("Property's Location")
                agent = request.form.get("ResponsibleAgent")
                sale_status = request.form.getlist("SaleStatus")
                tenure_type = request.form.getlist("TenureType")
                facilities = request.form.getlist("Facilities")
                #return saved and corrected pathway list of photos to this propDetImgsPaths variable
                propDetImgsPaths = SavedIMG(propDetImgs)
                print(f"Paths returned from SavedIMG: {propDetImgsPaths}")  # Debugging step
                if not propDetImgsPaths:
                    return "No images uploaded.", 400
                img = propDetImgsPaths[0]
                print(f"Main image: {img}")
                indexJson = json_add_property(name, img, propDetImgsPaths, property_description, price, property_lot_size, bedroom_number, bathroom_number, property_type, location, agent, sale_status, tenure_type, facilities)
                indexPropertyList.append(indexJson)

        with open("index_property.txt", "w") as file:
            indexPropertyList = json.dumps(indexPropertyList)
            file.write(indexPropertyList)
        return redirect("/admin/add_property")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        query = db.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';")

        if len(query) == 1:
            print(query)
            session["username"] = username
            session["admin"] = query[0]['ADMIN'] 
            return redirect('/')
        
        else:
            return render_template('login.html')
        
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cPassword = request.form['passwordC']
        
        if password != cPassword:
            return render_template('regFail.html')

        db.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{password}');")

        return redirect('/login')
    
@app.route("/admin/viewUser", methods=["GET","POST"])
def viewUser():
    if request.method == 'GET':
        query = db.execute("SELECT * FROM users;")
        print(query)
        return render_template('viewU.html',query=query)
    
@app.route("/logout", methods=["GET","POST"])
def logout():
    session.clear()
    return redirect('/')
      
if __name__ == "__main__":
    app.run(debug=True)

def json_add_property(name, img, propDetImgsPaths, property_description, price, property_lot_size, bedroom_number, bathroom_number, property_type, location, agent, sale_status, tenure_type, facilities):
    jsonDict = {"property_name" : name, "img_main_url" : img, "propDetImgs": propDetImgsPaths, "property_description": property_description, "price": price, "property_lot_size": property_lot_size, "bedroom_number": bedroom_number, "bathroom_number": bathroom_number, "property_type" : property_type, "property_location": location, "responsible_agent" : agent, "sale_status" : sale_status, "tenure_type": tenure_type, "facilities": facilities}
    #jsonPropertyDict = json.dumps(jsonDict)
    return jsonDict

'''def SavedIMG(imgs):
    saved_paths = []
    if not imgs:
        print("No images uploaded.")
        return saved_paths

    for img in imgs:
        if img.filename == '':
            print("Empty filename detected, skipping.")
            continue
        # Save files in the 'static/uploads' directory
        upload_folder = os.path.join('static', 'uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        filepath = os.path.join(upload_folder, img.filename)
        img.save(filepath)
        # Return the file path relative to the static folder
        saved_paths.append(filepath)

    print(f"Saved image paths: {saved_paths}")
    return saved_paths'''

def SavedIMG(imgs):
    saved_paths = []
    if not imgs:
        print("No images uploaded.")
        return saved_paths

    upload_folder = os.path.join('static', 'uploads')

    # Ensure the upload directory exists
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    for img in imgs:
        if img.filename == '':
            print("Empty filename detected, skipping.")
            continue

        # Sanitize the filename to remove spaces and special characters
        filename = img.filename.replace(" ", "_")
        filepath = os.path.join(upload_folder, filename)
        
        try:
            img.save(filepath)  # Save the file
            # Use relative path for rendering on the front-end
            relative_path = filepath.replace("\\", "/")  # Ensure consistency across OS
            saved_paths.append(relative_path)
        except Exception as e:
            print(f"Error saving file {filename}: {e}")

    print(f"Saved image paths: {saved_paths}")
    return saved_paths



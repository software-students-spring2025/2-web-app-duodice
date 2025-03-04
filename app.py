from flask import Flask, render_template, request, url_for, redirect, session
#import pymongo
from bson.objectid import ObjectId
import database
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import certifi
from dotenv import load_dotenv
from flask_session import Session


'''
notes / instructions

run app.py, then go to 127.0.0.1:5000 in browser

'''

# load environment variables 
load_dotenv()

# connect MongoDB
uri = os.getenv("MONGO_URI")
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
Mongo_DBNAME= os.getenv("MONGO_DBNAME")
myDb= client[Mongo_DBNAME]

app = Flask(__name__, static_folder='assets')

# start new user session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



# homepage / dashboard
@app.route("/", methods=('GET', 'POST'))
def show_dashboard():

    # if we are NOT logged in - redirect to login
    if 'userid' not in session or session['userid'] is None:
        return redirect(url_for('show_login'))
    print(session)
    print(session['userid'])
    # if we are logged in (session["userid"] is not None) - load the dashboard page
    # show the dashboard
    if request.method == "GET":   
        
        if 'userid' in session and session['userid'] is not None:
            data = {
                "user": database.get_user_info(myDb, ObjectId(session['userid'])),
                "deadlines": database.get_deadlines(myDb, ObjectId(session['userid'])), 
                "classes": database.get_classes(myDb, ObjectId(session['userid'])), 
                "tasks": database.get_tasks(myDb, ObjectId(session['userid'])) 
            }
            for i in range(0, len(data["deadlines"])):
                data["deadlines"][i]["_id"] = str(data["deadlines"][i]["_id"])
                data["deadlines"][i]["user_ID"] = str(data["deadlines"][i]["user_ID"])
                data["deadlines"][i]["class_ID"] = str(data["deadlines"][i]["class_ID"])
            for i in range(0, len(data["classes"])):
                data["classes"][i]["_id"] = str(data["classes"][i]["_id"])
                data["classes"][i]["user_ID"] = str(data["classes"][i]["user_ID"])
        
              
            
            return render_template('dashboard.html', data=data) # render home page template 
        
        
        
    
    # form handling
    elif request.method == "POST":
        pass  

    return render_template('dashboard.html') # render home page template 


# study session page
@app.route("/study", methods=('GET', 'POST'))
def show_study():

    # if we are NOT logged in - redirect to login
    if 'userid' not in session or session['userid'] is None:
        return redirect(url_for('show_login'))

    # show study session page
    if request.method == 'GET':
        data = {
                "user": database.get_user_info(myDb, ObjectId(session['userid'])),
                "deadlines": database.get_deadlines(myDb, ObjectId(session['userid'])), 
                "classes": database.get_classes(myDb, ObjectId(session['userid'])), 
                "tasks": database.get_tasks(myDb, ObjectId(session['userid'])), 
                "study-sessions": database.get_study_sessions(myDb, ObjectId(session['userid']))
            }
        return render_template('study_session.html', data=data) # render home page template 


# login
@app.route("/login", methods=('GET', 'POST'))
def show_login():
    # simply show the blank login page
    if request.method == "GET":   
        return render_template('signin.html', data={"error": ""}) # render home page template 
    
    # if information has been submitted to login: 
    elif request.method == "POST":
        uname = request.form['username']
        pwd = request.form['password']
        
        # authenticate the username and password
        uid = database.pwd_auth(myDb, uname, pwd)

        # incorrect username/password: reload page
        if uid is None:
            return render_template('signin.html', data={"error": "The username or password entered is incorrect."})

        # correct username/password: redirect to the dashboard
        session["userid"] = str(uid)
        return redirect(url_for('show_dashboard'))
    

# sign up / new account
@app.route("/signup", methods=("GET", "POST"))
def show_signup():
    # simply show the blank signup page
    if request.method == "GET":   
        return render_template('signup.html', data={"error": ""}) # render home page template 
    
    # if information has been submitted to signup: 
    elif request.method == "POST":
        uname = request.form['username']
        pwd = request.form['password']
        
        # try new account creation
        uid = database.new_account(myDb, uname, pwd)

        # if unsuccessful (user already exists)
        if uid is None: 
            return render_template('signup.html', data={"error": "This username is taken"})

        # set session variables
        # redirect to the dashboard
        session["userid"] = str(uid)
        return redirect(url_for('show_dashboard'))
    

# profile
@app.route("/profile", methods=("GET", "POST"))
def show_profile():

    # if we are NOT logged in - redirect to login
    if 'userid' not in session or session['userid'] is None:
        return redirect(url_for('show_login'))
    
    # simply show the profile page
    if request.method == "GET":   
        
        data = {
            "user": database.get_user_info(myDb, ObjectId(session['userid']))
        }
        return render_template('profile.html', data=data) # render profile page template 
    
    # 
    elif request.method == "POST":
        pass


# sign out
@app.route("/logout", methods=["GET"])
def logout():
    # edit session variables
    # redirect to the login page
    session["userid"] = None
    return redirect(url_for('show_login'))


# edit profile
@app.route("/profile-edit", methods=["POST"])
def edit_profile():
    pic = request.form['pic']
    name = request.form['name']
    age = request.form['age']
    bio = request.form['bio']
    print("profile edited in backend")
    data = {
        "user": {
            "userID": "",
            "name": name,
            "age": age,
            "username": "John", 
            "bio": bio
        }
    }
    return redirect(url_for('show_profile'))


# add class
@app.route("/add-class", methods=["POST"])
def add_class():
    # add class details to mongodb
    database.add_class(myDb, session["userid"], request.form["classname"])
    # reload dashboard
    return redirect(url_for("show_dashboard"))


# add deadline 
@app.route("/add-deadline", methods=['POST'])
def add_deadline():
    # add deadline details to mongodb
    database.add_deadlines(myDb, session["userid"], request.form["classid"], request.form["due-date"], request.form["name"], request.form["type"])
    # reload dashboard
    return redirect(url_for("show_dashboard"))

# edit deadlines
@app.route("/edit-deadlines", methods=['POST'])
def edit_deadlines():
    # get all deadlines 
    dlines = database.get_deadlines(myDb, ObjectId(session["userid"]))

    # iterate through them
    for d in dlines:
        did = str(d["_id"])
        if request.form[did + "-name"] != d["name"] or request.form[did + "-due-date"] != d["due_date"] or request.form[did + "-type"] != d["type"]:
            database.edit_deadline(myDb, did, request.form[did + "-name"], request.form[did + "-due-date"], request.form[did + "-type"])
            

    # add deadline details to mongodb
    #database.add_deadlines(myDb, session["userid"], request.form["classid"], request.form["due-date"], request.form["name"], request.form["type"])
    # reload dashboard
    return redirect(url_for("show_dashboard"))

# delete deadline 
@app.route("/delete-deadline", methods=['POST'])
def delete_deadline():
    # delete deadline from mongo
    database.delete_deadline(myDb, session["userid"], request.form["deadline-id"])
    # reload dashboard
    return redirect(url_for("show_dashboard"))

# delete class 
@app.route("/delete-class", methods=['POST'])
def delete_class():
    # delete class from mongo
    database.delete_class(myDb, session["userid"], request.form["classid"])
    # reload dashboard
    return redirect(url_for("show_dashboard"))

# keep alive
if __name__ == "__main__":
    app.run(debug=True) #running your server on development mode, setting debug to True

# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement

A web application that helps students track their study sessions, manage their time effectively, and analyze their study habits.

## User stories

Link to User Stories: https://github.com/software-students-spring2025/2-web-app-duodice/issues

## Steps necessary to run the software

- Install and setup [MongoDB](https://www.mongodb.com/) [Server](https://www.mongodb.com/products/platform/atlas-database) + [Client](https://www.mongodb.com/try/download/shell)

- Create a .env in which you will store variables for your MongoDB Connection String and the cluster you will connect to.
    - You will use this to request access to the database in order to edit data for a user. 

- If desired, create a new python virtual environment to run this code and install packages.
    - Run these commands on terminal:
        - python -m venv env
        - source env/bin/activate
- Ensure all necessary packages are installed. 
    - See [requirements.txt](requirements.txt) for necessary libraries and installations.
    - Ensure each library has been installed within your virtual environment. 
- Run the app.py code in order to start up the website. 
- In your browser, navigate to the url "127.0.0.1:5000". 
- From here, you may create a new user account or login to an existing one. 
    - To view an account with a lot of information already populated, use the credentials "exampleuser" "password" (please keep edits to this user account to a minimum). 





## Task boards

- [Sprint 1](https://github.com/orgs/software-students-spring2025/projects/6)

- [Sprint 2](https://github.com/orgs/software-students-spring2025/projects/17)

# Virtual Enviroment  dependeces:  
python -m pip install "pymongo[srv]"
pip install --upgrade certifi
# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement

A web application that helps students track their study sessions, manage their time effectively, and analyze their study habits.

## User stories

Link to User Stories: https://github.com/software-students-spring2025/2-web-app-duodice/issues

## Steps necessary to run the software

Install and setup [MongoDB](https://www.mongodb.com/) [Server](https://www.mongodb.com/products/platform/atlas-database) + [Client](https://www.mongodb.com/try/download/shell)
Users will also need to install flask in order to run the sowftware

Create a .env and store your MongoDB Connection String in a variable and store the cluster you want to connect to in a variable 
You will need to request acess to the database in order to edit data for a user
Run these commands on terminal:
- python -m venv env
- source env/bin/activate

Ensure you are loading your env variables into the code file

Test to establish connection with MongoDB and upon successfull connection you are successful

run the app.py code in order to start up the website. A url should be generated, copy and paste the url into the web in order to acess the website

See [requiremnets.txt](requirements.txt) for necessary libraries and installations.
Ensure all libraries have been installed within your virtual enviornment

## Task boards

- [Sprint 1](https://github.com/orgs/software-students-spring2025/projects/6)

- [Sprint 2](https://github.com/orgs/software-students-spring2025/projects/17)

# Virtual Enviroment  dependeces:  
python -m pip install "pymongo[srv]"
pip install --upgrade certifi
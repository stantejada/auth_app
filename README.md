# **Flask Authentication App**
### **A simple authentication system built with Flask, Jinja2, Bootstrap, and SQlite (SQLAlquemy)**
This project demonstrates how to implement user registration, login, and session management in a Flask web application.
## Table of Content.
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
6. [Authors](#authors)
8. [Acknowledgements](#acknowledgements)

## Installation
### Prerequisites:
* Python 3.8+
* Flask
* SQLAlchemy
* Bootstrap 5
### Instructions:  
1. Clone the repository  
   ```git clone https://github.com/stantejada/auth_app.git```  
2. Navigate to the project directory  
   ```cd auth_app```  
3. Create a virtual enviroment and activate it   
   ```python -m venv venv```  
   ```source venv/bin/activate #on window use 'venv\Scripts\activate'```  
4. Install the dependencies  
   ```pip install -r requirements.txt```  
5. Set up the database  
   ```flask db init```  
   ```flask db migrate -m "Initial migration."```  
   ```flask db upgrade```
6. Run the app
   ``` flask run ```  
   
## Usage  
Once the server is running, you can access the application at *http://127.0.0.1:5000/*  
### Main routes
* /register: Register a new user.
* /login: Log in with an existing user account.
* /index: Access the dashboard (requires authentication).
* /logout: Log out (lost access to home or index

### Example of use    
* Register a new user at `http://127.0.0.1:5000/register`
* Log in with your credentials at `http://127.0.0.1:5000/login`
* After logging in, you will be redirected to the homepage.
  
## Features
* **User Registration:** Allows new users to sign up with their username, email and password  
* **User Login:** Authenticated users can log in with their credentials.  
* **Session Management:** Uses Flask sessions to keep users logged in across different pages.  
* **Dashboard Access:** Authenticated users can access a protected dashboard  

## Authors
* **Diego Tejada** - @stantejada
  
## Acknowledgements
* Thanks to the Flask community for providing excellent resources and tutorials.
* Bootstrap for the responsive design components.
* SQLAlchemy for the ORM.
* Special thanks to the [Mega Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg for being an invaluable resource in learning Flask.

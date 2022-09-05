from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.users import User # this imports the User class from the users.py file inside the models folder

@app.route('/') # default route
def index():
    return redirect('/users')

@app.route('/users') # main page showing users in a table
def users():
    return render_template("users.html", users=User.get_all()) # users variable has access to all the table data on the users

@app.route('/user/new') # route to make a new user
def new():
    return render_template("new_users.html") # renders html page with form to make new user

@app.route('/user/create', methods=['POST']) # route that submits the info from the form on the new_users.html page
def create():
    print(request.form)
    User.save(request.form) # saves new user and their info from the form
    return redirect('/users')

@app.route('/user/edit/<int:id>') # route to edit a user
def edit(id):
    data = {
        "id": id
    } # this "data" dict makes it possible to use the user id key on the html page and on the route address
    return render_template("edit_user.html", user=User.get_one(data)) # user variable allows html page to use the keys based on one users id

@app.route('/user/update', methods=['POST']) # route that submits the info from the form on the edit_users.html page
def update():
    User.update(request.form) # uses class method to replace the new form info for the users table data
    return redirect('/users') # go back to home

@app.route('/user/show/<int:id>') # route to show users info
def show(id):
    data = {
        "id": id
    } # this "data" dict makes it possible to use the user id key on the html page and on the route address
    return render_template("show_user.html", user=User.get_one(data)) # user variable allows html page to use the keys based on one users id

@app.route('/user/destroy/<int:id>') # route to delete a user and their table data
def destroy(id):
    data = {
        'id': id
    } # this "data" dict makes it possible to use the user id key on the html page and on the route address
    User.destroy(data) # uses destroy class method to delete a user and their table data
    return redirect('/users') # redirect to home
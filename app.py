"""Blogly application."""

from flask import Flask, request, redirect, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from flask_migrate import Migrate

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'anotherone'

connect_db(app)
db.create_all()
migrate = Migrate(app, db)

@app.route('/')
def go_to_form():
    """go to form page"""
#should this be a redirect?
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def create_single_user_from_info():
    """receive and process data from form"""
    new_user = User(
        first_name = request.form['first'],
        last_name = request.form['last'],
        picture = request.form['picture']
    )

    db.session.add(new_user)
    db.session.commit()
#create list of User objects
    users = User.query.all()
    
    return render_template('users.html', users=users)

@app.route('/users/<int:id>')
def create_single_user(id):
    """put the user's information on own page"""
#return user object
    user_object=User.query.get(id)
    # iid = user_object['id']
    # first = user_object.get['first_name']
    # last = user_object.get['last_name']
    # img = user_object.get['picture']
    # iid = user_object['id']
    # iid = user_object.id
    # first = user_object.get.first_name
    # last = user_object.get.last_name
    # img = user_object.get.picture
    return render_template('single_user.html', user_object=user_object)    
    # return render_template('single_user.html', first=first, last=last, picture=img, iid=iid)


@app.route('/single_user_edit/<int:id>')
def edit_single_user(id):
    """put the user's information on own page"""

    return render_template('edit_user.html', id=id)


@app.route('/single_user_delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/')


@app.route('/submit_form/edit/<int:id>', methods=['POST'])
def create_user_from_info(id):
    """receive and process data from form"""
    user_object = User.query.get(id)
    user_object.first_name = request.form['first']
    user_object.last_name = request.form['last']
    user_object.picture = request.form['picture'] 

    db.session.add(user_object)
    db.session.commit()
#create list of User objects
    users = User.query.all()
    
    return render_template('users.html', users=users)

@app.route('/add_user')
def add_user():
    """go to add_user form page"""

    return render_template('add_user.html')
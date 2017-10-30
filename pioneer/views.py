# coding: utf-8
from . import app, login_manager
from flask import render_template, request, session, url_for, redirect, jsonify
from flask_login import login_required, current_user, login_user, logout_user
from .models import User

# NOTE: temporarily save user with dict. Will use database later
# {username1:{'id':$id, 'password':$password}, ...}
# id : 0:unknown 1~:user
users = {}
totid = 0

def authenticate(username, password):
    global users
    try:
        passwd = users[username]['password']
        if password == passwd:
            return True
    except KeyError:
        return False
    return False

@login_manager.user_loader
def load_user(user_id):
    global totid
    if user_id not in range(totid):
        return None
    user = User()
    user.id = user_id
    return user

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if authenticate(request.form['username'], request.form['password']):
            user = User()
            user.id = users[request.form['username']]['id']
            login_user(user)
            return jsonify({'role':session['user_id'], 'state':1})
        return jsonify({'role':0, 'state':0})
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        global totid, users
        totid += 1
        users.update(
            {
                request.form['username'] :
                {
                    'id':totid,
                    'password':request.form['password']
                }
            }
        )
        return redirect('/')
    return render_template('register.html')

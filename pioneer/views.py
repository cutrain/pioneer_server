from . import app, login_manager
from flask import render_template, request, session, url_for, redirect, jsonify
from flask_login import login_required, current_user, user_logged_in

@login_manager.user_loader
def load_user(user_id):
    # TODO: return user object
    return None

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if check_login(request.form['username'], request.form['password']):
            # TODO: fix this
            user_logged_in()
            return jsonify({'role':User.get_id(session['username']), 'state':1})
        return jsonify({'role':0, 'state':0})
    return render_template('login.html')

# coding: utf-8
from . import app, login_manager
from flask import render_template, request, session, url_for, redirect, jsonify
from flask_login import login_required, current_user, login_user, logout_user
from .models import User

# NOTE: temporarily save user with dict. Will use database later
# users :   {username1:{'id':$id, 'password':$password, 'name':$name, 'token':$token}, ...}
# id :      0:unknown 1~:user
# bbs:      {forumNmae1:{'lastReplyName':$, 'lastReplyTime':$,'postId':$,'postTitle':$,'replyNum':$}...}
users = {}
totid = 0
bbs = {}

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


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'state':1})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            if authenticate(request.form['username'], request.form['password']):
                user = User()
                name = request.form['username']
                user.id = users[name]['id']
                login_user(user)
                return jsonify({
                    'id':user.id,
                    'name':name,
                    'role':0,
                    'state':1,
                    'token':users[name]['token']
                })
        except KeyError:
            pass
        return jsonify({
            'id':0,
            'name':'',
            'role':0,
            'state':0,
            'token':'',
        })
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

@app.route('/forum/getForumList', method='POST')
def getForumList():
    try:
        global bbs
        forumName = request.form['forumName']
        if forumName in bbs:
            return jsonify({
                'lastReplyName':bbs['lastReplyName'],
                'lastReplyTime':bbs['lastReplyTime'],
                'postId':bbs['postId'],
                'postTitle':bbs['postTitle'],
                'replyNum':bbs['replyNum'],
            })
    except KeyError:
        pass
    return jsonify({
        'lastReplyName':'',
        'lastReplyTime':'',
        'postId':'',
        'postTitle':'',
        'replyNum':'',
    })

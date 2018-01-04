from .. import app, db, auth
from ..models import Users
from flask import request, jsonify
import time
import json


@app.route('/login', methods=['POST'])
def login():
    # TODO: login & modify database
    inform = ''
    try:
        data = json.loads(request.get_data().decode('utf-8'))
        username = data['username']
        password = data['password']
        user = Users.query.filter_by(username=username).first()
        if user is not None and password == user.password:
            user.token = user.generate_token()
            db.session.commit()
            return jsonify({
                'id':user.userId,
                'name':user.username,
                'role':user.role,
                'state':200,
                'token':user.token
            })
        else:
            inform = 'password error'
    except KeyError:
        inform = 'username or password is not specified'
    return jsonify({
        'id':0,
        'name':'',
        'role':0,
        'state':404,
        'token':'',
        'info': inform
    })

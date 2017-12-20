from .. import app, db
from ..models import Users
from flask import request, jsonify
import time


@app.route('/login', methods=['POST'])
def login():
    # TODO: login & modify database
    try:
        username = request.form.get('username')
        password = request.form.get('password')
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
    except KeyError:
        pass
    return jsonify({
        'id':0,
        'name':'',
        'role':0,
        'state':404,
        'token':'',
    })

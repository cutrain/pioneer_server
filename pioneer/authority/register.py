from .. import app, db
from flask import request, abort, jsonify
from ..models import Users
import json

@app.route('/register', methods=['POST'])
def register():
    # TODO: register
    data = json.loads(request.get_data())
    try:
        username = data['username']
        password = data['password']
        mail = data['mail']
    except KeyError:
        return jsonify({'state':400, 'info':'lack of [username, password, mail]'})
    if Users.query.filter_by(username=username).first() is not None:
        return jsonify({'state':400, 'info':'username already used'})
    user = Users(username=username, password=password, mail=mail, role=0)
    db.session.add(user)
    db.session.commit()
    return jsonify({'state':200})

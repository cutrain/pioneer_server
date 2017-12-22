from .. import app, db
from flask import request, abort, jsonify
from ..models import Users

@app.route('/register', methods=['POST'])
def register():
    # TODO: register
    username = request.form.get('username')
    password = request.form.get('password')
    mail = request.form.get('mail')
    if any(i is None for i in [username, password, mail]):
        abort(400)
    if Users.query.filter_by(username=username).first() is not None:
        abort(400)
    user = Users(username=username, password=password, mail=mail, role=0)
    db.session.add(user)
    db.session.commit()
    return jsonify({'state':200})

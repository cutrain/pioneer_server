from .. import app, db
from ..models import Users


@app.route('/login', methods=['POST'])
def login():
    # TODO: login & modify database
    try:
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()
        if user is not None and password == user.password:
            return jsonify({
                'id':user.userId,
                'name':user.nickname,
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

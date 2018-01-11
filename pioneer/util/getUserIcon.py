from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates
from flask import request, jsonify, g, send_from_directory
import json

@app.route('/util/getUserIcon', methods=['POST'])
@auth.login_required
def getUserIcon():
    return jsonify({
        'iconUrl':'/util/getPic/1'})
    try:
        data = json.loads(request.get_data().decode('utf-8'))
        typ = data['type']
        inf = data['userInfo']
        user = Users.query.filter_by(username=inf).first()
        if user is None:
            return jsonify({
                'iconUrl':'',
                'info':'user is not exists',
            })
        else:
            return jsonify({
                'iconUrl':user.iconlink
            })
    except KeyError:
        return jsonify({
            'iconUrl':'',
            'info':'type or userInfo doesn\'t specify'
        })

@app.route('/util/getPic/<int:num>', methods=['GET'])
def getPic(num):
    return send_from_directory('pics', 'icon.jpg', as_attachment=True)

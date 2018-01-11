from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates
from flask import request, jsonify, g
import json


@app.route('/forum/addToFavorite', methods=['POST'])
@auth.login_required
def addToFavorite():
    try:
        data = json.loads(request.get_data().decode('utf-8'))
        postId = data['postId']
        userId = g.user.userId
        favorite = Favorates(postId=postId, userId=userId)
        db.session.add(favorite)
        db.session.commit()
        return jsonify({
            'stateCode': 404
        })
    except KeyError:
        pass
    return jsonify({
        'stateCode': 404
    })


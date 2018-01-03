from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates
from flask import request, jsonify, g
import json


@app.route('/forum/getMyFavorite', methods=['POST'])
@auth.login_required
def getMyFavorite():
    try:
        userId = g.user.userId
        favorite = Favorates.query.filter_by(userId=userId)
        if favorite is not None:
            return jsonify({
                "postIds": [postId.postId for postId in favorite]
            })
    except KeyError:
        pass
    return jsonify({
        "stateCode": 404
    })
from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates
from flask import request, jsonify, g
import json


@app.route('/forum/getMyPosts', methods=['POST'])
@auth.login_required
def getMyPosts():
    try:
        userId = g.user.userId
        posts = Posts.query.filter_by(userId=userId).all()
        if posts is not None:
            return jsonify({
                "postIds": [id.postId for id in posts]
            })
    except KeyError:
        pass
    return jsonify({
        "stateCode": 404
    })
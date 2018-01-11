from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates
from flask import request, jsonify, g

@app.route('/forum/getMyReply', methods=['POST'])
@auth.login_required
def getMyReply():
    try:
        userId = g.user.userId
        reply = Replies.query.filter_by(userId=userId).all()
        retlists =  [id.postId for id in reply]
        retlists = list(set(retlists))
        if reply is not None:
            return jsonify({
                "postIds": retlists
            })
    except KeyError:
        pass
    return jsonify({
        "stateCode": 404
    })
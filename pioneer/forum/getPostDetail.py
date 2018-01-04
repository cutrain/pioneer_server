from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates
from flask import request, jsonify
import json

@app.route('/forum/getPostDetail', methods=['POST'])
@auth.login_required
def getPostDetail():
    try:
        data = json.loads(request.get_data().decode('utf-8'))
        postId = data['postId']
        post = Posts.query.filter_by(postId=postId).one()
        replies = Replies.query.filter_by(postId=post.postId).order_by(Replies.replyTime).all()
        return jsonify({
            'stateCode': 200,
            'title' : post.postTitle,
            'content' : replies[0].content,
            'replies' : [getReplyInfo(reply) for reply in replies]
        }) 
    except KeyError:
        pass
    return jsonify({
        'stateCode': 404
    })

def getReplyInfo(reply):
    info = {}
    info['floor'] = reply.floor
    info['user'] = Users.query.filter_by(userId=reply.userId).one().username
    info['content'] = reply.content
    info['likes'] = 0
    return info

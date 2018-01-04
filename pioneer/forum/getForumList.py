from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates
from flask import request, jsonify
import json

@app.route('/forum/getForumList', methods=['POST'])
@auth.login_required
def getForumList():
    try:
        data = json.loads(request.get_data().decode('utf-8'))
        forumName = data['forumName']
        posts = Posts.query.filter_by(forumName=forumName).all()
        return jsonify({
            'stateCode': 200,
            'postList': [getPostInfo(post) for post in posts]
        }) 
    except KeyError:
        pass
    return jsonify({
        'stateCode': 404
    })

def getPostInfo(post):
    info = {}
    info['postId'] = post.postId
    info['postTitle'] = post.postTitle
    info['postUser'] = Users.query.filter_by(userId=post.userId).one().username
    replies = Replies.query.filter_by(postId=post.postId).all()
    info['lastReplyTime'] = max(reply.replyTime for reply in replies)
    info['replyNum'] = len(replies)
    return info

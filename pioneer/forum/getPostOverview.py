from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates
from flask import request, jsonify
import json
from .getForumList import getPostInfo

@app.route('/forum/getPostOverview', methods=['POST'])
@auth.login_required
def getPostOverview():
    try:
        data = json.loads(request.get_data().decode('utf-8'))
        postId = data['postId']
        post = Posts.query.filter_by(postId=postId).one()
        return jsonify({
            'stateCode': 200,
            'postList': [getPostInfo(post)]
        }) 
    except KeyError:
        pass
    return jsonify({
        'stateCode': 404
    })

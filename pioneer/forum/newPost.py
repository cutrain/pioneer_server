from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates
from flask import request, jsonify, g
from flask.ext.login import current_user
from datetime import datetime
import json


@app.route('/forum/newPost', methods=['POST'])
@auth.login_required
def newPost():
    # print (g.user)
    # print (g.user.username)
    try:
        data = json.loads(request.get_data())
        title = data['title']
        content = data['content']
        forumname = data['forumName']
        postTime= datetime.now()
        userId = g.user.userId
        print('title ' + title)
        print('content ' + content)
        print('forumName ' + forumname)
        print('postTime' + str(postTime))
        posts = Posts(postTitle=title, forumName=forumname, postTime=postTime, userId=userId)
        print(posts.postId)
        db.session.add(posts)
        db.session.commit()
        reply = Replies(content=content, replyToId=userId, replyTime=postTime, userId=userId, postId=posts.postId, floor=1)

        db.session.add(reply)
        db.session.commit()
        return jsonify({
            'state': 200
        })
    except KeyError:
        pass
    return jsonify({
        'state': 404
    })
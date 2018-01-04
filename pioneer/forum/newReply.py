from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates
import json
from flask import request, jsonify, g
from datetime import datetime


@app.route('/forum/newReply', methods=['POST'])
@auth.login_required
def newReply():
    try:
        data = json.loads(request.get_data())
        content = data['content']
        postId = data['postId']
        replyToId = data['replyTo']
        postTime = datetime.now()
        userId = g.user.userId
        # reply = Replies(content=content, replyToId=replyToId, postId=postId)
        floorNum = Replies.query.filter_by().all()
        floornum = 1
        if floorNum is not None:
            for i in floorNum:
                if i.floor > floornum:
                    floornum = i.floor
        floornum += 1
        reply = Replies(content=content, replyToId=replyToId, replyTime=postTime, userId=userId, postId=postId, floor=floornum)
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
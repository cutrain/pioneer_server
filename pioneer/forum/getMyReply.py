from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates


@app.route('/forum/getMyReply', methods=['POST'])
@auth.login_required
def getMyReply():
    # TODO
    pass

from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates


@app.route('/forum/newReply', methods=['POST'])
@auth.login_required
def newReply():
    # TODO
    pass

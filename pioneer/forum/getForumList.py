from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates


@app.route('/forum/getForumList', methods=['POST'])
@auth.login_required
def getForumList():
    # TODO
    pass

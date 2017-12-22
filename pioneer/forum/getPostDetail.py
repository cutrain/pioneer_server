from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates


@app.route('/forum/getPostDetail', methods=['POST'])
@auth.login_required
def getPostDetail():
    # TODO
    pass

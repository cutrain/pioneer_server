from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates


@app.route('/forum/getMyPosts', methods=['POST'])
@auth.login_required
def getMyPosts():
    # TODO
    pass

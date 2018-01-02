from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates


@app.route('/forum/newPost', methods=['POST'])
@auth.login_required
def newPost():
    # TODO
    pass

from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates

@app.route('/forum/addToFavorite', methods=['POST'])
@auth.login_required
def addToFavorite():
    # TODO
    pass

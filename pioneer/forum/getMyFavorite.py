from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates


@app.route('/forum/getMyFavorite', methods=['POST'])
@auth.login_required
def getMyFavorite():
    # TODO
    pass

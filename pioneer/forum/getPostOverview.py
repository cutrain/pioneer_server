from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates


@app.route('/forum/getPostOverview', methods=['POST'])
@auth.login_required
def getPostOverview():
    # TODO
    pass

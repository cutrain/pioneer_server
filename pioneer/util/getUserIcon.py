from .. import app, db, auth
from ..models import Users, Posts, Replies, Likes, Favorates

@app.route('/util/getUserIcon', methods=['POST'])
@auth.login_required
def getUserIcon():
    # TODO
    pass

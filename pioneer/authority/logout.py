from .. import app, db, auth
from flask import g, jsonify


@app.route('/user/logout', methods=['POST'])
@auth.login_required
def logout():
    g.user.token = None
    db.session.commit()
    return jsonify({'state':200})

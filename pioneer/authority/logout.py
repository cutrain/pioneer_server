from .. import app, db, auth
from flask import g


@app.route('/logout', methods=['POST'])
@auth.login_required
def logout():
    g.user.token = None
    return jsonify({'state':200})

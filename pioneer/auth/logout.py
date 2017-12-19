from .. import app, db


@app.route('/logout', methods=['POST'])
def logout():
    # TODO: logout
    return jsonify({'state':0})

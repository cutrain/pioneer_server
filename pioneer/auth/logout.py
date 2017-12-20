from .. import app


@app.route('/logout', methods=['POST'])
def logout():
    return jsonify({'state':200})

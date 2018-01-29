from flask import Flask, jsonify, redirect, request, abort, url_for
import os
from users import MockUserDAO

userDao = MockUserDAO()
port = os.environ.get('PORT', 3000)
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return "Not Found", 404

@app.route('/users', methods=['GET'])
def list():
    users = userDao.find_all()
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def retrive(user_id):
    user = userDao.find_one(user_id)
    if user:
        return jsonify(user)
    return abort(404)

@app.route('/users', methods=['POST'])
def create():
    username = request.form.get('username')
    password = request.form.get('password')
    userDao.create(username, password)
    return redirect('/users')

@app.route('/users/<int:user_id>', methods=['PUT'])
def update(user_id):
    username = request.form.get('username')
    password = request.form.get('password')
    if userDao.update(user_id, username, password):
        return redirect(url_for('retrive', user_id=user_id))
    return abort(404)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    if userDao.remove(user_id):
        return '', 204
    return abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=port)

from flask import Blueprint, jsonify, request
from uuid import uuid4
import database.user_sql as sql

user_route = Blueprint('user', __name__, url_prefix='/user')

@user_route.route('/list/', methods=['GET'])
def list_user():
    user_list = sql.list_user()
    return jsonify(user_list), 200

@user_route.route('/create/', methods=['POST'])
def create_user():
    #user = request.json
    user = ["id", "name", "email", "active"]

    user[0] = str(uuid4())
    user[1] = request.form['name']
    user[2] = request.form['email']
    user[3] = request.form['active']
    
    sql.save_user(user)
    return jsonify(user), 201

@user_route.route('/update/', methods=['PUT'])
def update_user():
    #user = request.json
    user = ["id", "name", "email", "active"]

    user[0] = request.form['id']
    user[1] = request.form['name']
    user[2] = request.form['email']
    user[3] = request.form['active']
    
    sql.update(user)
    return jsonify(user), 201

@user_route.route('/find/', methods=['GET'])
def find_user():
    name = request.args.get('name')
    founded = sql.find_by_name(name)
    return jsonify(founded), 200

@user_route.route('/<uuid>/', methods=['DELETE'])
def delete_user(uuid):
    sql.delete(uuid)
    return jsonify({'message': 'User removed'}), 200
import flask
from flask import jsonify, request

from data import db_session
from data.users import User

blueprint = flask.Blueprint('users_api', __name__,
                            template_folder='templates')


@blueprint.route('/api/users')
def get_users():
    session = db_session.create_session()
    users = session.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(
                    only=('id', 'name', 'surname', 'email', 'hashed_password'))
                    for item in users]
        }
    )


@blueprint.route('/api/users/<int:user_id>')
def get_user(user_id):
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'users':
                user.to_dict(
                    only=('id', 'name', 'surname', 'email', 'hashed_password'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def add_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'name', 'surname', 'email', 'password']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    exist = session.query(User).filter(User.id == request.json['id']).first()
    if exist:
        return jsonify({'error': 'Id already exists'})
    user = User(
        id=request.json['id'],
        name=request.json['name'],
        surname=request.json['surname'],
        email=request.json['email'],
    )
    user.set_password(request.json['password'])
    user.password = request.json['password']
    session.add(user)
    session.commit()
    return jsonify({'success': 'OK (user added)'})


@blueprint.route('/api/users/delete/<int:user_id>', methods=['POST', "GET"])
def delete_user(user_id):
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return jsonify({'error': 'Not found (no such user)'})
    session.delete(user)
    session.commit()
    return jsonify({'success': 'OK (user deleted)'})


@blueprint.route('/api/users/change/<int:user_id>', methods=['POST'])
def change_user(user_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return jsonify({'error': 'not Found (no such user)'})
    if not any([key in request.json for key in
                ['name', 'surname', 'email', 'password']]):
        return jsonify({'error': 'bad request'})
    session.delete(user)
    for key in request.json:
        if key == 'name':
            user.name = request.json['name']
        if key == 'surname':
            user.surname = request.json['surname']
        if key == 'email':
            user.email = request.json['email']
        if key == 'password':
            user.set_password(request.json['password'])
    session.add(user)
    session.commit()
    return jsonify({'success': 'OK (user has changed)'})

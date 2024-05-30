#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from api.v1.utils import generate_token
#from flasgger.utils import swag_from


@app_views.route('/users', methods=['GET'], strict_slashes=False)
#@swag_from('documentation/user/all_users.yml')
def get_users():
    """Retrieves the list of all users"""
    all_users = storage.all(User).values()
    user_list = []
    for user in all_users:
        user_list.append(user.to_dict())
    return user_list

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
#@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_user(user_id):
    """ Retrieves a single user """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    
    return jsonify(user.to_dict())

@app_views.route('/users/number/<phone_number>', methods=['GET'], strict_slashes=False)
#@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_user_with_phonenumber(phone_number):
    """ Retrieves a single user using phone nmber"""
    user = storage.get_user_with_phone_no(phone_number)
    if not user:
        abort(404)
    
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
#@swag_from('documentation/user/delete_user.yml', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a user Object
    """

    user = storage.get(User, user_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
#@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_user():
    """
    Creates a user
    """
    

    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()

    if 'phone_number' not in data:
        abort(400, description="Missing phone number")
    if 'password' not in data:
        abort(400, description="Missing password")

    # Get user phone number
    phone_number = data.get('phone_number')

    # check if user exist
    user = storage.get_user_with_phone_no(data.get('phone_number'))
    if user:
        abort(400, description="User already exist")

    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict(), 201))

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
#@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def put_user(user_id):
    """
    Updates a user
    """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'email', 'phone_number', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
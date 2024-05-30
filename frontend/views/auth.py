#!/usr/bin/python3
"""flask authentication for craftdot"""

from flask import flash, Blueprint, current_app, jsonify, render_template, abort, request, redirect, url_for, make_response
import requests
from flask_login import login_user, logout_user, login_required, current_user
from frontend.loginmodel import User
from frontend.config import EXPIRATION_TIME
from api.v1.utils import generate_code
import datetime
import jwt



SECRET_KEY = 'fksdf7ehgbdbdc' #app.config['SECRET_KEY']
auth_bp = Blueprint("auth", __name__, url_prefix='/auth')



@auth_bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """logics for the home page"""


    if request.method == 'POST':
        # Get the login data converted to dict
        login_data = request.form.to_dict()
        # Get Phone number and password
        phone_number = login_data['phone_number']
        password = login_data['password']

        #get the user object with phone number
        url = f'http://127.0.0.1:8000/api/v1/users/number/{phone_number}'
        response = requests.get(url)
        if response.status_code == 200:
            user_data = response.json()
            user = User(user_data)
            login_user(user)
            flash(user_data, 'success')
            next = request.args.get('next')
            return redirect(next or url_for('service.service'))
        elif response.status_code == 404:
            flash("User not found", "error")
            return redirect(url_for('auth.login'))

        else:
            flash("Error logging in", 'error')
            return redirect(url_for('auth.login'))

    else:
        if current_user.is_authenticated:
            # send flash msg when user is login
            flash("You are logged in", 'success')
            return redirect(url_for('main.home'))
        else:
            # send flash msg when user is not login
            #flash("Please log in", "info")
            return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """ View to register user"""

    if request.method == 'POST':
        if not request.get_json():
            abort(400, description="Not a JSON")
        data = request.get_json()
        # Get Phone number and password
        phone_number = data.get('phone_number')
        password = data.get('password')

        #get the user object with phone number
        url = f'http://127.0.0.1:8000/api/v1/users/number/{phone_number}'
        response = requests.get(url)
        if response.status_code == 200:
            user = response.json()
            # Check if user exist
            if user:
                abort(400, description="User already exist")
        else:
            # Generate otp for new user registration
            num = generate_code(data.get('phone_number'))

            # Get the app secret key and set expiration time for otp
            secret_key = current_app.config['SECRET_KEY']
            expiration_time = current_app.config['EXPIRATION_TIME']

            # Generate the jwt with phone number and the token
            token_payload = {
                'phone_number': phone_number,
                'password': password,
                'otp': num,
                'exp': datetime.datetime.utcnow() + expiration_time
            }

            
            token = jwt.encode(token_payload, secret_key, algorithm='HS256')
            return make_response(jsonify(token), 200)
            
    else:
        return render_template('auth/register.html')


    

    

    
@auth_bp.route('/verify/otp', methods=['POST'], strict_slashes=False)
def verify_code():
    """ confirm the otp and jwt """
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()

    if 'token' not in data:
        abort(400, description="Missing token")
    if 'otp' not in data:
        abort(400, description="Missing otp")
    
    # Get the token and verification code
    token = data.get('token')
    otp = data.get('otp')

    # Convert the otp to int
    try:
        otp = int(otp)
    except Exception:
        abort(400, description="Invalid OTP")


    # Decode the token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        print('payload.......', payload)
    except jwt.ExpiredSignatureError:
        abort(400, description="Token expired")
    except jwt.InvalidTokenError:
        abort(400, description="Invalid token")
    if payload['otp'] != otp:
        abort(400, description="Invalid OTP")
    
    return make_response(jsonify(True), 200)

@auth_bp.route('/successful-signup', methods=['GET'])
def success_signup():
    """logics for the home page"""
    
    return render_template(
        'auth/success.html'
    )

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out', 'success')
    return redirect(url_for('main.home'))




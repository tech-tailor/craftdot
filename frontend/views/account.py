#!/usr/bin/python3
"""flask user account for craftdot"""



from flask import flash, Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from flask_login import current_user, login_required
from frontend.loginmodel import User
import requests


account_bp = Blueprint("account", __name__, url_prefix='/account')


@account_bp.route('/profile')
@login_required
def profile():
    """user profiles algo"""

    # Get user id
    user_id = current_user.id
    api_url = f"http://127.0.0.1:8000/api/v1/users/{user_id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        user_data = response.json()
    else:
        user_data = None 
    return render_template(
        'account/profile.html',
        user_data=user_data,
    )

@account_bp.route('/password')
@login_required
def change_password():
    """ Change user password"""
    return render_template(
        'account/change_password.html',
    )

@account_bp.route('/my-tasks')
@login_required
def my_tasks():
    """ Change user password"""
    return render_template(
        'account/my_tasks.html',
    )

@account_bp.route('/notification')
@login_required
def notification():
    """ Change user password"""
    return render_template(
        'account/notification.html',
    )

#sample test to create artisan
@account_bp.route('/create', methods=['GET', 'POST'])
def create_artisan():
    """logics for the home page"""
    if request.method == 'POST':

        # Create artisans from the form data

        form_data = request.form.to_dict()
        #name = form_data['name']
        #skill = form_data['skill']
        #availability = form_data['availability']
        url = 'http://127.0.0.1:8000/api/v1/artisans'
       
        headers = {
            'Content-Type': 'application/json',
        }

        r = requests.post(url, json=form_data, headers=headers)
        if r.status_code == 201:
            flash('Artisan created successfully', 'success')
        else:
            flash('Failed to create artisan', 'danger')
        return render_template(
        'account/create_artisan.html',
        )
    
    if request.method == 'GET':
        service_url = 'http://127.0.0.1:8000/api/v1/services'
        # return all services data
        r = requests.get(service_url)
        if r.status_code == 200:
            services = r.json()
            print(services)
        else:
            services = None

        return render_template(
        'account/create_artisan.html',
        services=services
        )
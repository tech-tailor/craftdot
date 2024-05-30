#!/usr/bin/python3
"""flask """

from flask import flash, Blueprint, render_template, request, redirect, url_for
from datetime import datetime


main_bp = Blueprint("main", __name__)

@main_bp.route('/')
def home():
    """logics for the home page"""
    
    
    return render_template(
        'main/home.html'
    )

@main_bp.route('/contact-us')
def contact_us():
    """logics for the contact us page"""
    
    return render_template(
        'main/contact_us.html'
    )

@main_bp.route('/about-us')
def about_us():
    """logics for the about us page"""
    
    return render_template(
        'main/about_us.html'
    )

@main_bp.route('/privacy-policy')
def privacy_policy():
    """logics for the about us page"""
    
    return render_template(
        'main/privacy_policy.html'
    )



@main_bp.route('/learn', defaults={'topic': None})
@main_bp.route('/learn/<string:topic>')
def learn(topic=None):
    """logics for the learning page"""

    if topic is None:
        return render_template(
            'main/learn.html'
        )
    else:
        temlate_path = f"learn/{topic}.html"
        try:
            return render_template(
                temlate_path
            )
        except:
            msg = "No such leaarning"
            return render_template(
                'main/learn.html',
                msg=msg
            )
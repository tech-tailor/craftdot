#!/usr/bin/python3
""" Utiltiy fuctions that can be used"""

from flask import current_app
import random
import datetime
import jwt

def generate_code(phone_number):
    """ Generates a random code """
    num = random.randint(100000, 999999)
    print(phone_number, num)

    return num



def generate_token(phone_number):
    """Generate user token with the phone number"""
    expiration_time = current_app.config['EXPIRATION_TIME']
    secret_key = current_app.config['SECRET_KEY']


    num = generate_code('phone_number')

    # Generate the jwt with phone number and the token
    token_payload = {
        'phone_number': phone_number,
        'otp': num,
        'exp': datetime.datetime.utcnow() + expiration_time
    }

    token = jwt.encode(token_payload, secret_key, algorithm='HS256')
    return token

def get_percent_val(value, percent):
    """ Return the percentage of any value"""

    r = (percent * value) / 100
    res = round(r)
    
    # return the rounded value of the given percentage
    return res 
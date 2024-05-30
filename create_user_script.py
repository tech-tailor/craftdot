#!/usr/bin/python3
""" Create sample Services to populate the data"""

import requests

def create_user():
    """User creation"""
    phone_number = input("Enter your phone number: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    password = input("Enter your password: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    country = input("Enter your country: ")
    street_address = input("Enter your street address: ")
    profile_picture = input("Input your profile picture: ")

    data = {
        'phone_number': phone_number,
        'first_name': first_name,
        'last_name': last_name,
        'password': password,
        'city': city,
        'state': state,
        'country': country,
        'street_address': street_address,
        'profile_picture': profile_picture
    }

    user_url = "http://127.0.0.1:8000/api/v1/users/"
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.post(user_url, headers=headers, json=data)
    if r.status_code == 200:
        user = r.json()
        #user_id = user['id']
        print(r.content)
        #print("User created, Your user id is", user_id)

if __name__ == "__main__":
    create_user()
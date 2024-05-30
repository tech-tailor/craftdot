#!/usr/bin/python3
""" objects that handle all default RestFul API actions for services """
from models.service import Service
from models.user import User
from models.artisan import Artisan
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
#from flasgger.utils import swag_from
from geopy.distance import geodesic
from geopy.geocoders import Nominatim



def match_artisan(user_id, service_id):
    user = storage.get(User, user_id)
    artisan = storage.get(Artisan, artisan_id)
    if user:
        user_street_address = user.street_address
        user_city = user.city
        user_state = user.state
        user_country = user.country
    if artisan:
        # get user id of the artisan
        user_id = artisan.user_id
        user = storage.get(User, user_id)
        artisan_street_address = user.street_address
        artisan_city = user.city
        artisan_state = user.state
        artisan_country = user.country




def get_distance_with_lon_lat(user_id, artisan_id):
    user = storage.get(User, user_id)
    artisan = storage.get(Artisan, artisan_id)
    if user:
        user_lon = user.longitude
        user_lat = user.latitude
    if artisan:
        # get user id of the artisan
        user_id = artisan.user_id
        user = storage.get(User, user_id)
        artisan_lon = user.longitude
        artisan_lat = user.latitude

    user_location = (user_lon, user_lat)
    artisan_location = (artisan_lon, artisan_lat)
    return (user_location, artisan_location)
    #distance_km = geodesic()

def get_distance_with_addr(user_id, artisan_id):
    user = storage.get(User, user_id)
    artisan = storage.get(Artisan, artisan_id)
    if user:
        user_street_address = user.street_address
        user_city = user.city
        user_state = user.state
        user_country = user.country
    if artisan:
        # get user id of the artisan
        user_id = artisan.user_id
        user = storage.get(User, user_id)
        artisan_street_address = user.street_address
        artisan_city = user.city
        artisan_state = user.state
        artisan_country = user.country

    user_full_addr = (user_street_address, user_city, user_state, user_country)
    artisan_full_addr = (artisan_street_address, artisan_city, artisan_state, artisan_country)
    print(user_full_addr, artisan_full_addr)
    user_cordinate = get_coordinates('Wuse, Abuja, Municipal Area Council, Federal Capital Territory, Nigeria')
    artisan_cordinate = get_coordinates('Wuse Market Road, Wuse, Abuja, Municipal Area Council, Federal Capital Territory, 900285, Nigeria')
    
    distance_km = get_distance_between_2_cordinates(user_cordinate, artisan_cordinate)
    # returnuser_street_address, user_city, user_state, user_country
    # artisan_street_address, artisan_city, artisan_state, artisan_country
    return (user_cordinate, artisan_cordinate, distance_km )

def get_coordinates(address):
    """Get latitude and longitude coordinates for a given address."""
    geolocator = Nominatim(user_agent="your_application_name")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None
    
def get_distance_between_2_cordinates(user1, user2):
    """ Get distance between 2 cordinates"""
    distance_km = geodesic(user1, user2)
    return distance_km
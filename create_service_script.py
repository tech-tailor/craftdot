#!/usr/bin/python3
""" Create sample Services to populate the data"""

from models.service import Service
import models
from models import storage

def create_services():
    """Service creation"""
    service_name = input("Enter the name of the service: ")
    service_description = input("Enter the description of the service: ")

    service = Service(name=service_name, description=service_description)

    storage.new(service)
    storage.save()
    print('service created', service)

if __name__ == "__main__":
    create_services()
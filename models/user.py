#!/usr/bin/python3
"""user model"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from hashlib import md5

class User(BaseModel, Base):
    """User model that entails every details"""
    __tablename__ = "users"
    phone_number = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    longitude = Column(String(128), nullable=True)
    latitude = Column(String(128), nullable=True)
    street_address = Column(String(255), nullable=True)
    city = Column(String(255), nullable=True)
    state = Column(String(255), nullable=True)
    country = Column(String(255), nullable=True)
    profile_picture = Column(String(128), nullable=True)
    is_artisan = Column(Boolean, default=False)
    artisan = relationship("Artisan", uselist=False, back_populates="user")
    #reviews = relationship("Review", back_populates="user")
    #bookings = relationship("Booking", order_by=Address.id, back_populates="user")


    def __init__(self, *args, **kwargs):
        """initialise the user model"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
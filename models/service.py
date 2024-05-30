#!/usr/bin/python3
"""category model"""


import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

class Service(BaseModel, Base):
    """create different service categories"""
    __tablename__ = "services"
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    #artisans = relationship("Artisan", back_populates="service")
    #reviews = relationship("Review", back_populates="service")
    #bookings = relationship("Booking", back_populates="service")

    def __init__(self, *args, **kwargs):
        """initialise the user model"""
        super().__init__(*args, **kwargs)
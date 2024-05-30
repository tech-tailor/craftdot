#!/usr/bin/python3
"""category model"""


import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """create different service categories"""
    __tablename__ = "reviews"
    service_id = Column(String(60), ForeignKey('services.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    comment = Column(String(1024), nullable=False)
    rating = Column(Integer, nullable=False)
    #user = relationship("User", back_populates="reviews")
    #service = relationship("Service", back_populates="reviews")

    def __init__(self, *args, **kwargs):
        """initialise the user model"""
        super().__init__(*args, **kwargs)
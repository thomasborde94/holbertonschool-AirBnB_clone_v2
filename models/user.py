#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class User(BaseModel):
    """indiquer le nom de la table dans laquelle les
    instances de la classe seront stockées"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place', cascade='all, delete', backref='user')
    reviews = relationship('Review', cascade='all, delete', backref='user')
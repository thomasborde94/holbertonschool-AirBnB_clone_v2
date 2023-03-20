#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class User(BaseModel):
    """indiquer le nom de la table dans laquelle les
    instances de la classe seront stockées"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    """
    cette ligne de commande crée une relation entre l'utilisateur et les
    places qu'il possède. Si un utilisateur est supprimé, toutes les places
    qui lui sont associées seront également supprimées en cascade
    backref='user'permet accéder facilement à l'utilisateur associé à une place.
    """
    places = relationship('Place', cascade='all, delete', backref='user')
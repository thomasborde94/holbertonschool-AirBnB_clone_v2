#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class User(BaseModel, Base):
    """indiquer le nom de la table dans laquelle les
    instances de la classe seront stockées"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
                                # Permet également de supprimer les objets enfants
    places = relationship('Place', cascade='all, delete-orphan', backref='user')
    reviews = relationship('Review', cascade='all, delete', backref='user')

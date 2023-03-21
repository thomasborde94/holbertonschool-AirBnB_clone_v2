#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    """
    La relation entre Place et Amenity est une relation Many-to-Many
    secondary='place_amenity' pour indiquer que la table de liaison
    à utiliser pour la relation est place_amenity.
    """
    place_amenities = relationship('Place', secondary='place_amenity')
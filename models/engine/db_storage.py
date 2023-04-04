#!/usr/bin/python3
""" Defines the class DBStorage"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from os import getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base


class DBStorage():
    """defines the class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """initializes the class DBStorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """tries to find all instances of a class name"""
        allClass = [City, State, User, Place, Review, Amenity]
        instanceList = []
        dictionary = {}

        if cls is None:
            for i in range(len(allClass)):
                instanceList += self.__session.query(allClass[i]).all()
        else:
            instanceList += self.__session.query(cls).all()

        for instance in instanceList:
            key = "{}.{}".format(instance.__class__.__name__, instance.id)
            dictionary[key] = instance
        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)

        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()

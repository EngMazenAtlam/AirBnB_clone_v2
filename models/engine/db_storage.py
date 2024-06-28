#!/usr/bin/python3
from models.config import ENV_VAR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base

class DBStorage:
    """Database Storage class"""
    __engine = None
    __session = None

    classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }

    def __init__(self):
            self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"\
                                        .format(ENV_VAR['hbnb_usr'], ENV_VAR['hbnb_usr_pwd'],\
                                                ENV_VAR['hbnb_host'], ENV_VAR['hbnb_db']),\
                                        pool_pre_ping=True)
            if ENV_VAR['hbnb_env'] == 'test':
                    Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Querying a specific table in the db if cls is specified
        Otherwise all tables in db is queried
        """
        temp_dict = {}
        if cls is not None:
            if isinstance(cls, str):
                cls = globals().get(cls)
            if cls is not None:
                for obj in self.__session.query(cls).all():
                    temp_dict.update({f"{cls}.{obj.id}": obj})
        else:
            for value in DBStorage.classes.values():
                for obj in self.__session.query(value).all():
                    temp_dict.update({f"{value}.{obj.id}": obj})

        return temp_dict

    def new(self, obj):
        """
        add obj to current db session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes in th current db seession
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete obj from the current db session
        """
        if obj is not None:
            self.__session.delete(obj)
            self.save(self)

    def reload(self):
        """create all tables in the database,
        create the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory =  sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

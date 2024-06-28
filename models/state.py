#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.config import ENV_VAR
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # if ENV_VAR['hbnb_storage_type'] == 'db':
        # cities = relationship('City', back_populates='state',\
        #                   cascade="all, delete-orphan")

    if ENV_VAR['hbnb_storage_type'] == 'file':
        @property
        def cities(self):
            """Returns the list of City instances
            with state_id equals to the current State.id
            """
            file_storage = FileStorage()
            all_cities = file_storage.all('City')
            state_cities = []
            for city in all_cities:
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities

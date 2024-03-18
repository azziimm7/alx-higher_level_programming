#!/usr/bin/python3

"""
Create the class City that will map to a table of the same name
in the database

 Args:
    Base: The base class from which the City classe should inherit.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """ A class that contains information about cities
        Args:
            id (int): The city id
            name (str): The city's name
            stat_id (int): The state id that correspond to this city
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

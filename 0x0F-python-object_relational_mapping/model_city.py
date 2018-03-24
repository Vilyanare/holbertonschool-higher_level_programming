#!/usr/bin/python3
"""
Module containing the database model for city table
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """Class for city table"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship("State", back_populates='cities')

State.cities = relationship("City", order_by=City.id, back_populates='state')

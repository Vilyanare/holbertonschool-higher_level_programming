#!/usr/bin/python3
"""
Returns a list of all entries in cities table and what states they are in
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model_state import State
from model_city import City

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1], argv[2], argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

for s, c in session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id):
    print("{}: ({}) {}".format(s.name, c.id, c.name))

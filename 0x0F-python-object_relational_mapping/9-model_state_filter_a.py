#!/usr/bin/python3
"""
Queries states table for all states with an a in them
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model_state import State

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1], argv[2], argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

for instance in session.query(State).order_by(
        State.id).filter(State.name.like("%a%")):
    print("{}: {}".format(instance.id, instance.name))

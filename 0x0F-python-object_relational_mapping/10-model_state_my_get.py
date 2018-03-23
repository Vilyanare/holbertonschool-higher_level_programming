#!/usr/bin/python3
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model_state import State

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1], argv[2], argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

stateid = session.query(State.id).filter(State.name == argv[4]).first()
if stateid:
    print(stateid[0])
else:
    print("Not found")

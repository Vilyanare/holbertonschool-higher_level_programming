#!/usr/bin/python3
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


from model_state import State

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    argv[1], argv[2], argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

updatestate = session.query(State).filter_by(id=2).first()
updatestate.name = "New Mexico"
session.commit()

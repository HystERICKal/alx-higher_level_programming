#!/usr/bin/python3
'''Task 7'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    reslt = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]))
    Base.metadata.create_all(reslt)
    the_sesh = sessionmaker(bind=reslt)
    sesh = the_sesh()
    outcome = sesh.query(State).order_by(State.id)
    for state in outcome:
        print('{}: {}'.format(state.id, state.name))
    sesh.close()

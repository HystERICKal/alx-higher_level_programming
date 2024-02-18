#!/usr/bin/python3
'''Task 12'''
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
    the_state = sesh.query(State).get(2)
    the_state.name = 'New Mexico'
    sesh.add(the_state)
    sesh.commit()
    sesh.close()

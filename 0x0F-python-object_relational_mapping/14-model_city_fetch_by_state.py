#!/usr/bin/python3
""" Task 14"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    the_sesh = sessionmaker(bind=engine)
    sesh = the_sesh()
    for x in (sesh.query(State.name, City.id, City.name)
              .filter(State.id == City.state_id)):
        print(x[0] + ": (" + str(x[1]) + ") " + x[2])

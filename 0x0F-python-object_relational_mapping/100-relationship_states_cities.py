#!/usr/bin/python3
"""Advanced Task 100"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    reslt = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                          .format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(reslt)

    the_sesh = sessionmaker(bind=reslt)
    sesh = the_sesh()

    the_state = State(name='California')
    the_city = City(name='San Francisco')
    the_state.cities.append(the_city)

    sesh.add(the_state)
    sesh.add(the_city)
    sesh.commit()

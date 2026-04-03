#!/usr/bin/python3
"""Deletes all State objects with 'a' in the name"""

import sys
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, password, db),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Get all states with 'a' (case-insensitive)
    states = session.query(State).filter(
        func.lower(State.name).like('%a%')
    ).all()

    # Delete them
    for state in states:
        session.delete(state)

    session.commit()
    session.close()

#!/usr/bin/python3
"""Lists all State objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """Main execution"""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            user, password, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states ordered by id
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()

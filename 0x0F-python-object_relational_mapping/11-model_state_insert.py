#!/usr/bin/python3
"""import libraries"""
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    engine = create_engine('mysql://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    conn = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    s = State(name='Louisiana')
    session.add(s)
    session.commit()

    print(s.id)


if __name__ == "__main__":
    main()

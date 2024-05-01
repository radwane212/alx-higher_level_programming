#!/usr/bin/python3
"""import libraries"""
from model_state import Base, State
from sqlalchemy import create_engine, text
from sys import argv


def main():
    engine = create_engine('mysql://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    conn = engine.connect()
    out = conn.execute(text("SELECT * FROM states"))
    first = out.fetchone()
    if first:
        print('{}: {}'.format(first[0], first[1]))
    else:
        print('Nothing')


if __name__ == "__main__":
    main()

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
    for i in out:
        print("{}: {}".format(i[0], i[1]))


if __name__ == "__main__":
    main()

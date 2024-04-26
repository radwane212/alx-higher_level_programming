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
    for row in out:
        flag = 0
        if row[1] == argv[4]:
            print(row[0])
            flag = 1
            break

    if flag == 0:
        print("Not found")


if __name__ == "__main__":
    if len(argv) == 5:
        main()

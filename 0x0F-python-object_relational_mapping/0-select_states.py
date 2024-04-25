#!/usr/bin/python3
"""
List all cases from database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def main():
    args = sys.argv[1:]
    username = args[0]
    password = args[1]
    database = args[2]
    connection = MySQLdb.connect(
        user=username,
        password=password,
        db=database,
        host="localhost",
        port=3306
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()

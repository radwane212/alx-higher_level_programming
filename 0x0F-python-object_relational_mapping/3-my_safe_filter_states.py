#!/usr/bin/python3
"""import library"""
import sys
import MySQLdb


def main():
    """ main function"""
    dbconnect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = dbconnect.cursor()

    states = "SELECT * FROM states WHERE name = %s"
    try:
        cursor.execute(states, (sys.argv[4],))
        readlist = cursor.fetchall()
        for i in readlist:
            print(i)
    except Exception:
        pass
    finally:
        dbconnect.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        main()

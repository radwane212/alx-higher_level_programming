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

    cities = "SELECT cities.id, cities.name, states.name\
                FROM cities \
                JOIN states ON cities.state_id=states.id"
    try:
        cursor.execute(cities)
        readlist = cursor.fetchall()
        for i in readlist:
            print(i)
    except Exception:
        print("Error")
    finally:
        dbconnect.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main()

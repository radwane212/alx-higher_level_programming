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

    cities = "SELECT cities.name, states.name\
                FROM cities\
                JOIN states ON cities.state_id = states.id"
    try:
        cursor.execute(cities)
        readlist = cursor.fetchall()
        out = ""
        for i in readlist:
            if (i[1] == sys.argv[4]):
                out += i[0] + ", "
        out = out.rstrip(", ")
        print(out)
    except Exception:
        print("Error")
    finally:
        dbconnect.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        main()

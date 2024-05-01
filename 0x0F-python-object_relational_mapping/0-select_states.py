#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

def list_states(user, password, database):
    try:
        # Establish a connection to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=database,
        )

       
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)
    finally:
        # Close the cursor and the database connection
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <user> <password> <database>")
        sys.exit(1)

    list_states(sys.argv[1], sys.argv[2], sys.argv[3])

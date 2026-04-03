#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cur = db.cursor()

    # Use format but safely
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_searched,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

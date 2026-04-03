#!/usr/bin/python3
"""
Lists all states starting with N from the database
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """Connects to MySQL and filters states"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cur = db.cursor()

    # 🔥 ONLY CHANGE FROM TASK 0
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC"
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

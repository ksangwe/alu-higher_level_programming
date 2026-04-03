#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
It takes 4 arguments: mysql username, mysql password, database name, state name.
It is safe from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name, charset="utf8")
    cursor = db.cursor()

    # SQL query: join cities with states, filter by state name (safe using placeholders)
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    # Print city names comma-separated
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()

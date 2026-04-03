#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
This script is safe from SQL injection and uses only one execute() call.
Usage: ./5-filter_cities.py <mysql username> <mysql password> \
<database name> <state name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <user> <passwd> <db> <state>")
        sys.exit(1)

    user, passwd, db_name, state_name = sys.argv[1], sys.argv[2], \
                                       sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=db_name,
                         charset="utf8")
    cursor = db.cursor()

    # SQL query safe from injection
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    # Print city names separated by commas
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()

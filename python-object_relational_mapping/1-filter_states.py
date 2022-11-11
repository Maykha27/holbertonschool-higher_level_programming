#!/usr/bin/python3
# Lists all states with a name starting with N from the database hbtn_0e_0_usa.
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

import MySQLdb
import sys


if__name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    for state in cursor.fetchall():
        if state[1][0] == "N":
            print(state)

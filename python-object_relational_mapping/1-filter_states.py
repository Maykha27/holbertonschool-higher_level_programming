#!/usr/bin/python3
"""
lists all states with a name
starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb


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

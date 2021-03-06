#!/usr/bin/python3
"""
Queries states table for user provided state
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    s = "SELECT id, name FROM states WHERE name = (%s) ORDER BY id"
    cur.execute(s, [argv[4]])
    rows = cur.fetchall()

    for x in range(len(rows)):
        print("{}".format(rows[x]))

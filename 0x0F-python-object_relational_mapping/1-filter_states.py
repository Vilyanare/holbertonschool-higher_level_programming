#!/usr/bin/python3
"""
Queries states table for all entries that start with N
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name like 'N%' ORDER BY id")
    rows = cur.fetchall()

    for x in range(len(rows)):
        print("{}".format(rows[x]))

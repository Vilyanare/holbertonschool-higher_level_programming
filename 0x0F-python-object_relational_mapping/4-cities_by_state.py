#!/usr/bin/python3
"""
Queries for cities and assigns state names by id from state table
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    s = ("SELECT cities.id, cities.name, states.name "
        "FROM cities INNER JOIN states "
        "ON cities.state_id=states.id ORDER BY cities.id")
    cur.execute(s)
    rows = cur.fetchall()

    for x in range(len(rows)):
        print("{}".format(rows[x]))

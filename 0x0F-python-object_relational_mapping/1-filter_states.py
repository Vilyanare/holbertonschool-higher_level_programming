#!/usr/bin/python3
import MySQLdb
from sys import argv

db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()
cur.execute("SELECT id, name FROM states WHERE name like 'N%' ORDER BY id")
rows = cur.fetchall()

for x in range(len(rows)):
    print("{}".format(rows[x]))

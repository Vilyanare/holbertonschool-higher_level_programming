#!/usr/bin/python3
import MySQLdb
from sys import argv

db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()
s = ("SELECT cities.name FROM cities "
     "INNER JOIN states ON cities.state_id=states.id "
     "WHERE states.name = %s ORDER BY cities.id")
cur.execute(s, [argv[4]])
rows = cur.fetchall()

cs = False

for x in rows:
    if cs:
        print(", ", end='')
    print("{}".format(x[0]), end='')
    cs = True
print()

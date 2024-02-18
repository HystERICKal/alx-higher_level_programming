#!/usr/bin/python3
"""  listing all the states """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    v = db.cursor()
    v.execute("""SELECT * FROM states WHERE name LIKE\
    '{:s}' ORDER BY id ASC""".format(argv[4]))
    for row in v.fetchall():
        print(row)
    v.close()
    db.close()

#!/usr/bin/python3
"""  listing all the states """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    v = db.cursor()
    exact = argv[4]
    v.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (exact,))
    reslt = list(row[0] for row in v.fetchall())
    print(*reslt, sep=", ")
    v.close()
    db.close()

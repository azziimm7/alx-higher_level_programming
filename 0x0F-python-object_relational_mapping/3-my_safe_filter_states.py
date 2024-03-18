#!/usr/bin/python3
""" this module lists all states from a given DB"""
import sys
import MySQLdb

if __name__ == "__main__":
    connect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM states \
            WHERE name LIKE BINARY %s", (sys.argv[4],))
    query = cursor.fetchall()
    for row in query:
        print(row)
    cursor.close()
    connect.close()

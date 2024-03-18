#!/usr/bin/python3
""" this module lists all cities from a given DB"""
import sys
import MySQLdb

if __name__ == "__main__":
    connect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    cursor = connect.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states on cities.state_id = states.id\
            ORDER BY cities.id ASC")
    query = cursor.fetchall()
    for row in query:
        print(row)
    cursor.close()
    connect.close()

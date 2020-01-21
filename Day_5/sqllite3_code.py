import csv

import sqlite3

conn=sqlite3.connect('zoo.db')

#creating cursor

c=conn.cursor()
#c.execute(""" CREATE TABLE zoo( animal TEXT,uniq_id INTEGER,water_need INTEGER)""")


with open('zoo.csv') as zoo_file:
    csv_reader=csv.reader(zoo_file,delimiter=',')
    next (csv_reader)
    for i in csv_reader:
        c.execute("""INSERT INTO zoo VALUES('{}',{},{})""".format (str(i[0]),i[1],i[2]))
c.execute("select * from zoo")

for i in c.fetchall():
    print str(i[0]), " ", i[1], i[2]


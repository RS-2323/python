import mysql.connector
import csv
conn=mysql.connector.connect(user='root',password='bsdu@123',host='Localhost')
c=conn.cursor()

#c.execute("""CREARE DATABASE zoodb""");
c.execute("""use zoodb""");
with open('zoo.csv') as zoo_data:
    csv_reader=csv.reader(zoo_data,delimiter=',')
    next(csv_reader)
    for i in csv_reader:
        c.execute("""INSERT INTO zoodb.zoo VALUES('{}',{},{})""".format (str(i[0]),i[1],i[2]))
c.execute("select * from zoo")

for i in c.fetchall():
    print str(i[0]), " ", i[1], i[2]        
        

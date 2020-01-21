import csv
import sqlite3


print "enter 1 for bakery"
print "enter 2 for flights"

user_input=input("enter your choice>")

if(user_input==1):
    print "\nyour bakery database>"
    conn=sqlite3.connect('bakery.db')
    c1=conn.cursor()
    #c1.execute("""CREATE TABLE goods(id INTEGER,flavor TEXT,food TEXT,price INTEGER)""")
    with open ('goods.csv') as goods_file:
        csv_reader1=csv.reader(goods_file,delimiter=',')
        next(csv_reader1)
        for goods in csv_reader1:
            
            c1.execute("""INSERT INTO goods VALUES ('{}','{}','{}','{}')""".format(goods[0],goods[1],goods[2],goods[3])) 
    c1.execute("""SELECT * FROM goods""")
    for i in c1.fetchall():
        print str(i[0])," ",i[1],i[2],i[3]
                          
if(user_input==2):
    print "\nyour flight database>"
    conn=sqlite3.connect('flights.db')
    c2=conn.cursor()
    #c2.execute("""CREATE TABLE flights(Airline INTEGER,FlightNo INTEGER,SourceAirport TEXT,DestAirport TEXT)""")
    with open ('flights.csv') as flights_file:
        csv_reader2=csv.reader(flights_file,delimiter=',')
        next(csv_reader2)
        for flights in csv_reader2:
            c2.execute("""INSERT INTO flights VALUES({},{},{},{})""".format(flights[0],flights[1],flights[2],flights[3])) 
    c2.execute("SELECT * FROM flights")
    for i in c2.fetchall():
        print str(i[0]), " ", i[1], flights[2],i[3]
                           



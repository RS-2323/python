#Write a program to create a sqlite database with python.
import mysql.connector
#for connect your sqlite
join = mysql.connector.connect(user='root', password="",host='localhost')
#create sqlite cursor cursor
c=join.cursor()
#for create database
c.execute("""CREATE DATABASE zoos;""")
#for use database
c.execute("""USE zoos""")



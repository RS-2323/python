#Write a program to read a CSV file and print its contents.---
#this is for open your CSV file on read mode---
my_file = open("zoo.csv","rt")

#this is for open your CSV file on write mode---
my_file2 = open("zoo.txt","wt")

#loop for read contents of your csv file line by line---
for i in my_file:
    
#write content in second file which is read in first file by read mode---
    my_file2.write( i )
    
#print your second file---
    print i
    
#close first file which is open in start---
my_file.close()

#close second file which is open in start---
my_file2.close()

#This is a program to read a text file.---
#this is for open your text file---
my_file = open('git_tute.txt','rt')

#for read text file which is save in your directory---
read_file = my_file.read()

#print your read file ---
print read_file

#close file which is open in start---
my_file.close()

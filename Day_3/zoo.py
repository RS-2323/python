my_file = open("zoo.csv","rt")

my_file2 = open("zoo.txt","wt")
for i in my_file:
    my_file2.write( i )
    print i
my_file.close()
my_file2.close()

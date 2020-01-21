'''
my_file = open('Static_RCA_change_report_for_20190105_091501.csv','rt')

print my_file

my_file.close()
'''
'''
my_file = open('b.txt','wt')
my_file.write("pooja\n")
my_file.write("Lokesh\n")
my_file.write("Ashwini\n")
my_file.write("Neha\n")
my_file.write("Lavish")
my_file.close()
'''
'''
my_file = open('a.txt','rt')

read_file = my_file.read()
print read_file

my_file.close()
'''

my_file = open('a.txt','rt')

read_file = my_file.readline()
print read_file

my_file.close()


my_file = open('a.txt','rt')

read_file = my_file.readlines()
for i in read_file:
    print i

my_file.close()

'''
my_file = open('a.txt','rt')

for i in my_file:
    print i

my_file.close()
'''
'''
my_file = open('a.txt','rt')
read_file = my_file.readlines()
for i in my_file:
    my_file = open('C:/Users/Om/Desktop/Ria_Sharma_Python/Day_2/d.txt','at')
    my_file.write(i)
my_file.close()
'''

# for save same file to another text file(copy to file with rename)
my_file = open('a.txt','rt')
my_file2 = open('d.txt','wt')
for i in my_file:
    my_file2.write(i)
    
my_file.close()
my_file2.close() 































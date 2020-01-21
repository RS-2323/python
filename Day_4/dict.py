import csv

dict1= {}


with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    next(csv_reader)
  #to skip the header from csv file
    
    for row in csv_reader:
        if row[0] not in dict1.keys():
            dict1[row[0]]=int(row[2])
        else:
            dict1[row[0]]=dict1[row[0]] + int(row[2])

for key,values in dict1.items():
    print 'total water drinken by {} = {}'.format(key,values)





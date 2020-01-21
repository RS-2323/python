import csv
count=0
water=0

#method 1(for print animal details)

with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    



    for row in csv_reader:
        print (row[2])

#method 1(for print animal name)
'''
with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')



    for row in csv_reader:
        print (row[0])
'''
#method 1(for print unique Id)
'''
with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')



    for row in csv_reader:
        print (row[1])
'''
#method 1(for print water need)
'''
with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')

animal,uniq_id,water_need

    for row in csv_reader:
        print (row[2])
'''

# For print total water needed in zoo
'''
water=0

with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')

    for row in csv_reader:
        if count==0:
            count=count+1
            continue
        water  = water+ int(row[2])
       
    
print 'total water drinken by animal is ={}'.format(water)
'''
#  Another Method For print total water needed in zoo
'''
water=0

with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    
#to skip the header from csv file
    
    next(csv_reader)

    for row in csv_reader:

        water  = water+ int(row[2])
       
    
print 'Total water drinken by animal is = {}'.format(water)

'''
'''
water=0

with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')

    for row in csv_reader:
        if count==0:
            count=count+1
            continue
        elif row[0]=='elephant':
            water  = water+ int(row[2])
       
    
print 'total water drinken by elephant is ={}'.format(water)

water1=0

with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')

    for row in csv_reader:
        if count==0:
            count=count+1
            continue
        elif row[0]=='tiger':
            water1  = water1+ int(row[2])
       
    
print 'total water drinken by tiger is ={}'.format(water1)

water2=0

with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')

    for row in csv_reader:
        if count==0:
            count=count+1
            continue
        elif row[0]=='zebra':
            water2  = water2+ int(row[2])
       
    
print 'total water drinken by zebra is ={}'.format(water2)

water3=0

with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')

    for row in csv_reader:
        if count==0:
            count=count+1
            continue
        elif row[0]=='kangaroo':
            water3 = water3+ int(row[2])
       
    
print 'total water drinken by kangaroo is ={}'.format(water)

with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')

    for row in csv_reader:
        if count==0:
            count=count+1
            continue
        elif row[0]=='lion':
            water  = water+ int(row[2])
       
    
print 'total water drinken by lion is ={}'.format(water)
'''
#second method
'''
water=0
water1=0
water2=0
water3=0
water4=0
water5=0

with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    
#to skip the header from csv file
    
    next(csv_reader)

    for row in csv_reader:
    

        if row[0]=='elephant':
            water  = water+ int(row[2])
        elif row[0]=='tiger':
            water1=water1+int(row[2])
        elif row[0]=='zebra':
            water2=water2+int(row[2])
        elif row[0]=='lion':
            water3=water3+int(row[2])
        elif row[0]=='kangaroo':
            water4=water4+int(row[2])

        water5=water+water1+water2+water3+water4
    print 'Total water drinken by animal is = {}'.format(water5)

    print 'Total water drinken by elephant is = {}'.format(water)
    print 'Total water drinken by tiger is = {}'.format(water1)
    print 'Total water drinken by zebra is = {}'.format(water2)
    print 'Total water drinken by lion is = {}'.format(water3)
    print 'Total water drinken by kangaroo is = {}'.format(water4)

'''
'''
water=0
water1=0
water2=0
water3=0
water4=0
water5=0  
with open('zoo.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
 
#to skip the header from csv file
    
    next(csv_reader)

    for row in csv_reader:
    

        if row[0]=='elephant':
            water  = water+ int(row[2])
        if row[0]=='tiger':
            water1=water1+int(row[2])
        if row[0]=='zebra':
            water2=water2+int(row[2])
        if row[0]=='lion':
            water3=water3+int(row[2])
        if row[0]=='kangaroo':
            water4=water4+int(row[2])

        water5=water+water1+water2+water3+water4
    print 'Total water drinken by animal is = {}'.format(water5)

    print 'Total water drinken by elephant is = {}'.format(water)
    print 'Total water drinken by tiger is = {}'.format(water1)
    print 'Total water drinken by zebra is = {}'.format(water2)
    print 'Total water drinken by lion is = {}'.format(water3)
    print 'Total water drinken by kangaroo is = {}'.format(water4)

'''











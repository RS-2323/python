#this is a frogram of Ria Sharma---
#This is a program to read zoo.csv and calculate water need for every animal.---
zoo_file = open("zoo.CSV","rt")
#inisilize the vale of water1,water2,water3,water4,water5,water6 ---
water1 =0
water2=0
water3=0
water4=0
water5=0
water6=0
#loop for read content from zoo_file and store in i---
for i in zoo_file:
#split zoo_file by ,---
    y=i.split(",")
#check animal file name--- 
    if  y[0]=="elephant":
#calculate water need by for loop---
        water1 = water1 +int(y[2])
#check animal second name ---
    elif y[0]=="tiger":
#calculate water need by for loop---
        water2=water2+int(y[2])
#check animal third name ---
    elif y[0]=="zebra":
#calculate water need by for loop---
        water3=water3+int(y[2])
#check animal forth name ---
    elif y[0]=="lion":
#calculate water need by for loop---
        water4=water4+int(y[2])
#check animal fifth name ---
    elif y[0]=="kangaroo":
#calculate water need by for loop---
        water5=water5+int(y[2])
#calculate water need by for loop---
water6=water1+water2+water3+water4+water5
#print total water need all animals---
print 'total water drinken by elephant is ={}'.format(water1)
print 'total water drinken by tiger is ={}'.format(water2)
print 'total water drinken by zebra is ={}'.format(water3)
print 'total water drinken by lion is ={}'.format(water4)
print 'total water drinken by kangaroo is ={}'.format(water5)
print '\ntotal water drinken by all animals is ={}'.format(water6)

zoo_file.close()

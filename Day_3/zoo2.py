zoo_file = open("zoo.CSV","rt")
water1 =0
water2=0
water3=0
water4=0
water5=0
water6=0

for i in zoo_file:
    y=i.split(",")
    if  y[0]=="elephant":
        water1 = water1 +int(y[2])
    elif y[0]=="tiger":
        water2=water2+int(y[2])
    elif y[0]=="zebra":
        water3=water3+int(y[2])
    elif y[0]=="lion":
        water4=water4+int(y[2])
    elif y[0]=="kangaroo":
        water5=water5+int(y[2])
water6=water1+water2+water3+water4+water5
print 'total water drinken by elephant is ={}'.format(water1)
print 'total water drinken by tiger is ={}'.format(water2)
print 'total water drinken by zebra is ={}'.format(water3)
print 'total water drinken by lion is ={}'.format(water4)
print 'total water drinken by kangaroo is ={}'.format(water5)
print '\ntotal water drinken by all animals is ={}'.format(water6)

zoo_file.close()


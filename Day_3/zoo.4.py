zoo_file = open("zoo.CSV","rt")
water =0
zoo_file1 = zoo_file.readline()
zoo_file2=zoo_file.readlines() 
for i in zoo_file2:
    y=i.split(',')
 
    water  = water+ int(y[2])
       
    

print 'total water drinken by animal is ={}'.format(water)
zoo_file.close()




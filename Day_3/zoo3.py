zoo_file = open("zoo.csv","rt")
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
for i in zoo_file:
    split_list=i.split(",")

    if  split_list[0]=='elephant':
        count1=count1+1
    elif  split_list[0]=='tiger':
        count2=count2+1
    elif  split_list[0]=='lion':
        count3=count3+1
    elif  split_list[0]=='zebra':
        count4=count4+1
    elif  split_list[0]=='kangaroo':
        count5=count5+1
count6=count1+count2+count3+count4+count5
print 'total elephant is ={}'.format(count1)
print 'total tiger is ={}'.format(count2)
print 'total lion is ={}'.format(count3)
print 'total zebra is ={}'.format(count4)
print 'total kangaroo is ={}'.format(count5)
print '\ntotal animal is ={}'.format(count6)
zoo_file.close()

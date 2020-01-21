name = raw_input("enter your Name>>>")
N= name.find(' ')


name1 = name[N:]
name2 = name[:N]

print name1[::-1],name2[::-1]

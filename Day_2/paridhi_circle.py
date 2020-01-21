"""
radius = 3.9
pi = 3.14
paridhi = 2*pi*radius
print paridhi

"""
"""
def paridhi_circle():
    radius = 6.9
    pi = 3.14
    paridhi = 2*pi*radius
    print paridhi

paridhi_circle()

"""
"""
def paridhi_circle(radius):
    pi = 3.14
    paridhi = 2*pi*radius
    return paridhi

my_paridhi = paridhi_circle(5.0)
print my_paridhi
print "circumfrence of circle = {}".format(my_paridhi)
"""
def paridhi_circle():
    radius = input("enter your radius>")
    pi = 3.14
    paridhi = 2*pi*radius
    return paridhi

my_paridhi = paridhi_circle()
print "circumfrence of circle = {}".format(my_paridhi)

    

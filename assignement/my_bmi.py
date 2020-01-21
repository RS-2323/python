#This is a program to calculate the BMI.---

#Define function for calculate Bmi---
def your_bmi():
    
#taking input from user for his/her height in feet---
    height_in_feet =input('enter your height in feet>')
    
#taking input from user for his/her height in inch---
    height_in_inch =input('enter your height in inch>')
    
#change height in meter which taking from user ni feet anf meter---
    height_In_meter=(height_in_feet*.3048)+(height_in_inch*0.0245)
    
#taking input from user for his/her weight in kg---
    weight=input("enter your weight in kg>")
    
#BMI formula is as given below ---    
    my_bmi = weight /(height_In_meter**2)
    
#print user bmi in their form of (kg)/(m2) by using format method---
    print "your Bmi is:{}".format(my_bmi)
    
#call function which is define at the code top---
your_bmi()

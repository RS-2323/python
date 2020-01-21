#foot/inch to meter calculater

#storing my height in feet

myHeightInFeet = input("enter your height in feet>")
myHeightInFeet = myHeightInFeet*.3048


#storing my height in inch

myHeightInInch = input("enter your height in inch>")

myHeightInInch = myHeightInInch*0.0254


#storing my height in meter

myHeightInMeter = myHeightInFeet + myHeightInInch

#get my height in meter

print myHeightInMeter

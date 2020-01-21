#my bmi

#storing my height in feet

myHeightInFeet = input("enter your height in feet>")

myHeightInFeet = myHeightInFeet*.3048

#storing my height in inch

myHeightInInch = input("enter your height in inch>")

myHeightInInch = myHeightInInch * 0.0254

#storing my height in meter

myHeightInMeter = myHeightInFeet + myHeightInInch

#storing my weight

myWeight = input("enter your weight>")

#get my bmi

myBmi = (myWeight)/(myHeightInMeter**2)

print myBmi

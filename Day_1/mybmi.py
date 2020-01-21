#myBmi
#storing my weight
myWeight = 36

#storing my height in feet
myHeightInFeet = 5 * 0.3048

#storing my height in inch
myHeightInInch = 1 * 0.0254

#storing my height in meter
myHeightInMeter = myHeightInFeet + myHeightInInch

#get my bmi

myBmi=(myWeight)/(myHeightInMeter**2)
print myBmi

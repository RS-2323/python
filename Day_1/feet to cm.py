# foot/inch to meter caculater
foot=.3048
inch=.0254
#this is your height in foot
myHeightfoot=input("Enter your height in foot>")
#this is my height in inch
myHeightinch=input("Enter your hight in inch>")
#this ia your height in meter
myHeightcm=(myHeightfoot*foot+myHeightinch*inch)*100
print(myHeightcm)

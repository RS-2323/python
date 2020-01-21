
#Average calculator of car in mile per gallon

#Vehical travelled in kilometer
distance_In_kilometer = input("enter the distance in kilometer >")

#fuel used in litre
fuel_Litre = input("Enter the fuel used in Litre >")

#litre in gallon
one_Litre = float(.264)

#kilometer in mile
one_Kilometer = float(.621)

#distance in mile
distance_In_mile = (distance_In_kilometer)*one_Kilometer

#fuel in gallon
fuel_In_gallon = (fuel_Litre)*one_Litre

#average of car in mpg
average_Of_car = (distance_In_mile)/float(fuel_In_gallon)

#final
print(average_Of_car)

#This is a program to find the prime Number.---
#inisilize the vale of number where we start to find prime number---
number =1

#taking input from user for find prime number limitation
use=input("enter number where as far as you find prime number>")

#print statement for user view---
print "\nprime number form 1 to {}>".format(use)

#first loop start form the number which we inisilize starting and  of user input---
while number <=use:
    
#inisilize the vale of i ---
    i=1
#here we check that i is <= number OR not---
    while i<=number:
        
#increse the vale of i for second while loop---
                i=i+1
                
#here we check that number is prime OR not---
                    if (number%i==0):
                        
#here we want that if number is divided by i then break the second loop---
#here we don't know that number is prime---
                            break
                        
#here we check that nuumber is = to i---
#if number is equal to i then print number with print statement---
            if i==number:
                
#print statement for number
                    print number
                    
#increse the vale of number for first while loop---      
            number = number +1 



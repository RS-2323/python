
#storing our game

#import random number

import random

secret_number = random.randint(1,10)
player_number = input("enter your guess number between 1 and 10>>>")

#condition making

if(player_number >1 and player_number <10):

#true condition for player
    
    if(secret_number == player_number):
        print("Player wins :) ! \nComputer lose :( !")
        print("you win :) !!! \ncongratulations")
#false condition for player

    else:
        if(secret_number>player_number):
            print("Computer guess high number compair to player")
        else:
            print("Player guess high number compair to computer")
        print("Computer generate = {}".format(secret_number))
        print("computer wins :) ! \nplayer lose :( !")
        
else:
    print("invalid number.Please enter again>>>")


#use while loop for program run again
    
n=0

#condition for program run only 6 times

while(n<5):
    secret_number = random.randint(1,10)
    player_number = input("\nenter your guess number between 1 and 10>>>")
    if(player_number >1 and player_number <10):
        if(secret_number == player_number):
            print("Player wins :) ! \nComputer lose :( !")
            print("you win :) !!! \ncongratulations")
   
#when player win game will break
            
            break
        else:
            if(secret_number>player_number):
                print("Computer guess high number compair to player")
            else:
                print("Player guess high number compair to computer")
            print("Computer generate = {}".format(secret_number))
            print("computer wins :) ! \nplayer lose :( !")
            
    else:
        print("invalid number.Please enter again>>>")
        
#print left chance which have player
        
    left=4-n
    print("left chance = {}".format(left))

#print this when game will over and o chance have user
    
    if(left==0):
        print("\nGame Over  :( !!! ")
        if(secret_number!=player_number):
            print("try next time")
        else:
            print("\ncongratulations")
    n=n+1

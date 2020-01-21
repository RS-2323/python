def show_help():
    #printing instructions on how to use app
    print("Enter 'DONE' in Caps to stop adding items.")
    print("Enter 'SHOW' in Caps to show list.")
    print("Enter 'HELP' in Caps to take help.")
def show_list():
         
     print("Here's the list.")
     for i in my_item:    
            print(i)
def add_to_list(name):
    split_item = item.split(',')
    
    # user item being added to the list
    my_item.extend(split_item)
    

# making empty list
my_item = []

#Making app shopping list
print("What should we pick at the store ?")

# Adding condition
while True:

    #ask for new items
    item= raw_input(">")

    #be able to quit the app
    if(item== 'DONE'):
        show_list()
        break
        
        
    #print out the list
    if(item == 'SHOW'):
        show_list()
        
       
            

     #print out the help for consumer       
    elif(item == 'HELP'):
        show_help()

   
    else:
        add_to_list('new_Item')
    

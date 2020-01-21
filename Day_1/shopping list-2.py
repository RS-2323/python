#make a list to hold onto oue items
shopping_list = []
#print out instructions on how to use the app
def show_help():
        print("What should we pick up at the store?")
        print("if you print 'DONE' shopping list is complete")

def show_func():
         for item in shopping_list:
            
            print item


#ask for new items
print("WELCOME!")
print("enter your item")

while True:
     
     my_item = raw_input(">")
     if my_item=="DONE" :
             print("here in your list item>")
      
             show_func()
             break
    
     elif my_item=="HELP" :
           show_help()

     elif my_item=="SHOW" :
                print("here in your recent  list item>")
        
                show_func()
             

     else:
            shopping_list.append(my_item)

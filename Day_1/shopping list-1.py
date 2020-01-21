#make a list to hold onto oue items

#print out instructions on how to use the app
print("What should we pick up at the store?")
print("if you print 'DONE' shopping list is complete")
print("enter your item")
shopping_list = []
#ask for new items
my_item = raw_input(">")
#add new items to our list

while(my_item !="DONE"):
     shopping_list.append(my_item)
     my_item = raw_input(">")
     
#be able to quit the app
print("here your list")
#print out the list
for item in shopping_list:
    print item
        
    





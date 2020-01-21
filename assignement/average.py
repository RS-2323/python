#10. Return the "centered" average of an array of integers,
#which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array.
#If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
#Use int division to produce the final average. You may assume that the array is length 3 or more.
numbers = list(input("Enter your numbers with comma seprated:"))
find_max = max(numbers)
find_min = min(numbers)
numbers.remove(find_max)
numbers.remove(find_min)
average=sum(numbers)
count = len(numbers)
print "Centersd average of user input is:{}".format(average/count)

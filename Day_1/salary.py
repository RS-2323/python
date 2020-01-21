# calculation salary

# storing workingHour
workingHour = 40

#storing base pay

basePay = input("enter your base pay>")

#storing salary

salary = (workingHour)*(basePay)

print("salary:")

print(salary)

#if employe work overtime

#storing total working hour

totalWorkingHour = input("enter your total working hour>")


#storing overtime

overtimeWorkHour = totalWorkingHour -  workingHour

#storing salary with overtime work

salaryWithOvertime = salary + (overtimeWorkHour)*(basePay*1.5)

lowTimeWorkHour =  workingHour - totalWorkingHour 

salaryWithLowtime = salary -(lowTimeWorkHour )*(basePay*0.5)

if(totalWorkingHour<40 and totalWorkingHour!=40):

    print ("salaryWithLowtime")

    print (salaryWithLowtime)

elif(totalWorkingHour==40):
        print("salary:5")
        print(salary)


else:
    print ("salaryWithOvertime")

    print (salaryWithOvertime)


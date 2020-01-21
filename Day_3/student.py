
st_name = open('student.txt','wt')

n=1
while(n<=3):
    student_name = raw_input ("enter  student name {}.>".format(n))
    
    st_name.write(student_name+'\n')
    n=n+1

    
st_name.close()
 
   
    
    

'''To accept student’s five courses marks and compute his/her result.
Student is passing if he/she scores marks equal to and above 40 in each course.
If student scores aggregate greater than 75%, then the grade is distinction.
If aggregate is 60>= and <75 then the grade if first division.
If aggregate is 50>= and <60, then the grade is second division.
If aggregate is 40>= and <50, then the grade is third division'''


sub_list=[]
num=int(input("how many subject"))
total_marks=num*100
print("total_marks",total_marks)
for i in range(num):
    mark=int(input("enter subjet marks"))
    sub_list.append(mark)
print("subject marks are",sub_list)

for i in range(len(sub_list)) :
               if(sub_list[i]<40 or sub_list[i]>100):
                   print("student fails")
               else :
                   aggregate=(sum(sub_list)*100)/total_marks
print("aggregate of studnet is",aggregate)

if(aggregate>=75) :
    print("student pass with distinction")
elif(aggregate >= 60 and aggregate <75 ):
    print("student pass with first division")    

elif(aggregate >= 50 and aggregate <60 ):
    print("student pass with second division")

elif( aggregate >= 40 and aggregate <50 ):
    print("student pass with third division")

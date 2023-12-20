class employee:
    empcount=0
    female_count=0
    male_count=0
    salary_count=0
    desig_count=0
    def __init__(self,name,desg,salary,gender):
        self.name=name
        self.desg=desg
        self.salary=salary
        self.gender=gender
        employee.empcount+=1
        if(self.gender=="f"):
            employee.female_count+=1
        else:
            employee.male_count+=1
        if(self.salary>10000):
            employee.salary_count+=1
        if(self.desg =="ass_manager"):
            employee.desig_count+=1

    def displaycount(self):
        print("there are %d employee"% employee.empcount)
    def displaygendercount(self):
        print("there are %d femal count"% employee.female_count)
        print("there are %d male"% employee.male_count)
    def displaysalarycount(self):
        print("there are %d salary"% employee.salary_count)
    def displaydesigcount(self):
        print("there are %d assistant manager"% employee.desig_count)
    def displaydetails(self):
        print("name:",self.name,"designation:",self.desg,"salary:",self.salary,"gender:",self.gender)

e1=employee("a","manager",10000,"f")
e2=employee("b","clerk",80000,"f")
e3=employee("c","manager",20000,"m")
e4=employee("d","ass_manager",90000,"m")
                            
e4.displaycount()
e4.displaygendercount()
e4.displaysalarycount()
e4.displaydesigcount()
print("details of emplyee")
e4.displaydetails()

'''Create class EMPLOYEE for
storing details(Name, designation, gender, Date of joining and Salary).
Define function members to compute
a) total number of employees in an organization
b) Count of male and female employee
c) Employee with salary more than 10,000
d) Employee with designation “Asst Manager”'''

class Employee:
    count=0
    female_count=0
    male_count=0
    salary_count=0
    desig_count=0
    def __init__(self,name,desig,gender,doj,salary):
        self.name=name
        self.desig=desig
        self.gender=gender
        self.doj=doj
        self.salary=salary
        Employee.count+=1
        if(self.gender=="F"):
            Employee.female_count+=1
        else:
            Employee.male_count+=1
        if(self.salary>10000):
            Employee.salary_count+=1
        if(self.desig =="Asst_manager"):
            Employee.desig_count+=1

    def display_emp_count(self):
        print("There are ",Employee.count, " employees in the organization")
    def count_gender(self):
        print("There are ",Employee.female_count, " female employees in the organization")
        print("There are ",Employee.male_count, " male employees in the organization")
    def count_big_salary(self):
        print("There are ",Employee.salary_count, " employees in the organization having salary >10000")
    def count_desig(self):
        print("There are ",Employee.desig_count, " employees in the organization with designation 'Asst_manager' ")

#Entering data for Employee class
e1=Employee("Chitra","manager","F","1-2-2001",50000)
e2=Employee("Ankita","Asst_manager","F","23-5-2007",20000)
e3=Employee("Varsha","Accountant","F","11-9-2010",10000)
e4=Employee("Rahul","HR","M","24-3-2012",30000)
e5=Employee("Aditya","Asst_manager","M","14-7-2009",20000)

e5.display_emp_count()
e5.count_gender()
e5.count_big_salary()
e5.count_desig()

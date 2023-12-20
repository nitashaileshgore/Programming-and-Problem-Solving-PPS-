#write a Program for ctreating student database using function and list

'''
personal_info()
rollno, name, class, emailid,  mobile no, adharcard,address
display_data()
'''
r=[]
n1=[]
c=[]
n=int(input("enetr how many students data u want to enter")) #global
def data_entry():
    for i in range(n):
        roll=int(input("enetr rollno"))
        r.append(roll)
        #r.append(input("enetr rollno"))
        n1.append(input("enetr name of student"))
        c.append(input("enetr student class"))
def display_data():
    print("rollno\t\tname\t\tclass")
    for i in range(n):
        print("{}\t\t{}\t\t{}".format(r[i],n1[i],c[i]))


data_entry()
display_data()


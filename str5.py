name=input("enter a name")
clas=input("enter a class")
r_no=int(input("enter rollno"))
per=float(input("enetr percentage"))
'''
print("name=",name)
print("class=",clas)
print("roll no=",r_no)
print("precentage=",per)
print("name=%s\n clas=%s\nr_no=%d\npercentage=%f"%(name,clas,r_no,per))
'''
print("name={n}\nclass={c}\nrollno={r}\nprecenatge={p}".format(n=name,c=clas,r=r_no,p=per))
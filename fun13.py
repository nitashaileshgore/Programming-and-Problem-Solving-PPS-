#Variable-length arguments or keywards varible argument or **kwargs
def subject_choice(name,*branch):
    print("name=",name)
    for i in branch:
        c=input("enetr your fav branch")
        if c==i:
            print("your fav branch is present in perticular clg so u can take admission")
            break

subject_choice("abc","comp","ETC","mech","civil")
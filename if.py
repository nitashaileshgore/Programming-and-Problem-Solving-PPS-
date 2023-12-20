che=int(input("enter marks for chem"))
math=int(input("enter marks for math"))
bee=int(input("enter marks for bee"))
mech=int(input("enter marks for mech"))
sme=int(input("enter marks for sme"))
if che>=40 and math>=40 and bee>=40 and mech>=40 and sme>=40:
    print("studnet is pass")
    avg=che+math+bee+mech+sme/5
    print("avg=",avg)
    if avg>=75:
        print("distinction")

else:
    print("student is fail")
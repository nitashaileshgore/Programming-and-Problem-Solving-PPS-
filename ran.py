import random
#1-10  ->random
s={6:4,9:2}
l={3:8,2:5}
p=p1=0
while(True):
    print("1.payer1 \n2.player2")
    c=int(input("enetr which player has a tern"))
    if c==1:
        a=random.randint(1,6)
        print(a)
        for i in s:
            if a ==i:
                p=p-s[i]
                print(p)
        for i in l:
            if a==i:
                p=p+l[i]
                print(p)
        if p==10:
            print("player1 is winner")
            break
    elif c==2:
        a1 = random.randint(1, 6)
        print("a1=",a1)
        p1 = p1 + a1
        if p1 == 10:
            print("player2 is winner")
            break
    else:
        print("no winner")
        break

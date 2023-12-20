import random2,sys
val=10
l={4:6,3:10}
s={5:1,7:2}

print("how many player")
p=int(input("enter no of player"))
val=val1=0
while(True):

    print("\\1.player1\n2.player2")
    c=int(input("enetr which player is playing"))
    if c==1:
        a=random2.randint(1,6)
        print(a)
        val=val+a
        print("val=",val)
        for i in l:
            if val==l.keys():
                    val=val+l[i]
            print("val=", val)
        for i in s:
            if val==s.keys():
                val=val-s[i]
            print("val=", val)
        if val==20:
            print("player 1 is winner")
            break
    elif c==2:
        b = random2.randint(1, 6)
        print(b)
        val1 = val1 +b
        print("val1=",val1)
        if val1 == 10:
            print("player 2 is winner")
            break
    else:
        print("enetr wrong choice")
        sys.exit(0)
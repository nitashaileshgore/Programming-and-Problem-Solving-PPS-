'''
1
1 2
1 2 3
1 2 3 4
'''
for i in range(1,10):  #outer loop
    print("\n")
    for j in range(1,i):  #inner loop
        print(j,end=" ")
'''
i=1  j=i=1     *
i=2  j=i=2->0,1 * *
i=3 j=3->0,1,2  * * *

'''
r=int(input("enter the no. of rows:"))
c=int(input("enter the no.of coloum :"))
matrix1=[]
print("enter number rowwise")
for i in range(r):
    a =[]
    for j in range(c):
        a.append(int(input()))
    matrix1.append(a)
for i in range(r):
    for j in range(c):
        print(matrix1[i][j],end=" ")
    print()
 # printing diagonal matrix
for i in range(r):
    print()
    for j in range(c):
         if i==j:
             print(matrix1[i][j],end=" ")
         elif j==(c-1):
             j=c-i-1
             print(matrix1[i][j],end=" ")
            
         else :
             matrix1[i][j]=0
             print(matrix1[i][j],end=" ")


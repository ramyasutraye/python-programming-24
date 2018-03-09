x=int(input("enter x"))
y=int(input("enter y"))
print(str(x)+" "+str(y))
for i in range(x+1,y):
    if(i%2==0):
        print(i,end=" ")

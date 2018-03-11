a=int(input("enter"))
b=int(input("enter2"))
for i in range(a,b):
    temp=i
    sum=0
    while(temp>0):
        digit=temp%10
        sum=digit**3
        temp//=10
    if(sum==n):
        print(sum)
            

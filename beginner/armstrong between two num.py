num=int(input("enter"))
n=int(input("enter 2"))
for i in range(num,n):
    temp=i
    sum=0;
    while(temp>0):
        digit=temp%10
        sum+=digit**3
        temp//=10
    if(sum==i):
        print(i)
   

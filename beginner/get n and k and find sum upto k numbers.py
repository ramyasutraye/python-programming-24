lst=[]
s=0
n=int(input("enter n"))
k=int(input("enter k"))
for i in range(n):
    lst.append(int(input()))
for i in range(k):
      s=s+lst[i]
print(s)

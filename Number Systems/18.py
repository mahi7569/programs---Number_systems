def pronic(n):  # 1 to n pronic numbers count and sum
    for i in range(1,n):
        p=i*(i+1)
        if p==n:
            return 1
n=int(input())
m=int(input())
c=0
s=0
for i in range(n,m+1):
    if pronic(i):
        c+=1
        s+=i
        print(i,end=' ')
print(' ')
print(c)
print(s)

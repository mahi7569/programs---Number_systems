def pronic(n):  # 1 to n pronic numbers
    for i in range(1,n):
        p=i*(i+1)
        if p==n:
            return 1
n=int(input())
m=int(input())
for i in range(n,m+1):
    if pronic(i):
        print(i,end=' ')

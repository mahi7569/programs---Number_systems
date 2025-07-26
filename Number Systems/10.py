def prime(n):  # print twine prime numbers 
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
m=int(input())
l=[]
for i in range(n,m):
    if prime(i):
        l.append(i)
for i in range(len(l)-1):
    if abs(l[i]-(l[i+1]))==2:
        print((l[i],l[i+1]))
''' The difference b/w 2 consective prime numbers which is equal to 2 '''

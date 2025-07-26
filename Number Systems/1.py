def prime(n):   ## print prime numbers b/w the given range
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
s=int(input())
e=int(input())
for i in range(s,e+1):
    if prime(i):
        print(i,end=' ')

def arm(n):  # prime numbers in a 1-n armstrong numbers
    s=0
    for i in str(n):
        s+=int(i)**len(str(n))
    if s==n:
        return 1
    else:
        return 0
def prime(n):
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
l=[]
for i in range(1,n+1):
    if arm(i):
        l.append(i)
print(l)
for i in l:
    if prime(i):
        print(i,end=' ')

def prime(n):  # first n prime numbers sum
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
#n=int(input())
k=int(input())
l=[]
for i in range(2,1000):
    if prime(i):
        l.append(i)
s=0
for i in l[:k]:
    s+=i
print(s)
    

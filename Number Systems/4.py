def prime(n):  # print Nth prime number
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
s=int(input())
e=int(input())
k=int(input())
l=[]
for i in range(s,e+1):
    if prime(i):
        l.append(i)
print(l)
print(l[k-1])
       

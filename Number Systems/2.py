def prime(n):  ## Prime numbers count
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
s=int(input())
e=int(input())
c=0
for i in range(s,e+1):
    if prime(i):
        print(i,end=' ')
        c+=1
print(' ')
print(c)

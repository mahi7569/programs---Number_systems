def magic(n):  # magic numbers from 1 to n and count, sum
    s=0
    for i in str(n):
        s+=int(i)
    if s*int(str(s)[::-1])==n:
        return 1
    else:
        return 0
n=int(input())
c,s=0,0
for i in range(1,n+1):
    if magic(i):
        print(i,end=' ')
        c+=1
        s+=i
print(' ')
print(c)
print(s)
    

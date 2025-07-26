def happy(n):# Happy Number 1 to n and count , sum
    l=[]
    while True:
        s=0
        for i in str(n):
            s+=int(i)*int(i)
        if s==1:
            return 1
        else:
            if s not in l:
                l.append(s)
            else:
                return 0
        n=s
n=int(input())
c=0
s=0
for i in range(1,n+1):
    if happy(i):
        print(i,end=' ')
        c+=1
        s+=i
print(' ')
print(c)
print(s)

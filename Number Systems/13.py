# Armstrong number 1 to n
def arm(n):
    
    s=0
    for i in str(n):
        s+=int(i)**len(str(n))
    if s==n:
        return 1
    else:
        return 0
n=int(input())
for i in range(1,n+1):
    if arm(i):
        print(i,end=' ')

        

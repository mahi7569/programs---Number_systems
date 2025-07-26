def happy(n):  # Happy number
    l=[]
    while(1):
        s=0
        while n!=0:
            r=n%10 
            s+=r**2
            n//=10
        if s==1:
            return 1 
            break 
        elif s not in l:
            l.append(s)
            n=s 
        else:
            return 0 
s=int(input())
e=int(input())
for i in range(s,e+1):
    if happy(i):
        print(i,end=" ")
    
            

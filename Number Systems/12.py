n=int(input())  # Armstrong number
s=0
for i in str(n):
    s+=int(i)**len(str(n))
if s==n:
    print("Yes")
else:
    print("No")
        

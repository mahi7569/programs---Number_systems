n=int(input())   ## num is prime power or not
if n&(n-1)==0 and n>0:
    print("Yes")
else:
    print("No")

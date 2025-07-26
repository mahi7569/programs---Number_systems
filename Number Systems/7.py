def prime(n): ## sum of individual digits and sum is prime or not
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
s=0
for i in str(n):
    s+=int(i)
if prime(s):
    print(s,"is a prime number")
else:
    print(s,"is not a prime number")
    
    

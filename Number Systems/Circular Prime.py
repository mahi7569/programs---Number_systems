def prime(n):  # Circular prime number
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1 
def is_prime(n):
    s=str(n)
    for i in range(len(s)):
        r=int(s[i:]+s[:i])
        if prime(r):
            return 1 
        else:
            return 0
n=int(input())
if is_prime(n):
    print("Yes")
else:
    print("No")

def prime(n):  # Check prime number by performing 2 steps
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
r=int(str(n)[::-1])
print(r)
if prime(int(str(n)[::-1])):
    print("Yes")
else:
    print("No")

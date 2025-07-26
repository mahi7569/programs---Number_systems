def prime(n): # print large and small prime factores
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
l1=[]
for i in l:
    if prime(i):
        l1.append(i)
print(l1)
print(l1[0],"is a min prime number",l1[-1],"is a max prime number")

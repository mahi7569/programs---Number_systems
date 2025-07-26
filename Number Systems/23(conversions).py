n=int(input())  # Decimal to Binary Conversion
res=''
while n!=0:
    res+=str(n%2)
    n//=2
print(res[::-1])

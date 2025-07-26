n=input()  # Binary to Decimal Conversion
dv=1
s=0
for i in n[::-1]:
    if i=='1':
        s+=dv
    dv=dv*2
print(s)

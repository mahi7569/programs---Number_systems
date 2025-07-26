n=int(input())
res=''
for i in (bin(n)[2:]):
    if i=='1':
        res+='0'
    else:
        res+='1'
print(int(res,2))
        

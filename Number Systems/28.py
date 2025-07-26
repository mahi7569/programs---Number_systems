n=int(input())
res=''
while n!=0:
    res+=str(n%2)
    n//=2
re=''
for i in res:
    if i=='1':
        re+='0'
    else:
        re+='1'
dv=1
s=0
for i in re:
    if i=='1':
        s+=dv
    dv=dv*2
print(s)
        

l=list(map(int,input().split()))
l1=set(l)
l2=[]
for i in l1:
    l2.append(l.count(i))
l3=[]
for i in l1:
    if max(l2)==l.count(i):
        l3.append(i)
print(max(l3))
    


def prime(n):  # print Next prime number 
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
def is_p(k):
    num=k+1
    while True:
        if prime(num):
            return num
        num+=1
k=int(input())
print(is_p(k))
        

n=int(input())   # Obtain palindrome number by using 2 steps
while True:
    s=0
    s=int(str(n)[::-1])+n
    if str(s)==str(s)[::-1]:
        print(s)
        break
    else:
        n=s

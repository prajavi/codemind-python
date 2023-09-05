n=int(input())
rev=0
t=n
n=(n**2)**0.5
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
q=int(rev)
if t>0:
    print(q)
else:
    print(f"-{q}")
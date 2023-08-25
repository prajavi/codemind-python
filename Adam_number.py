n=int(input())
re=0
rev=0
sq=n*n
while(n>0):
    r=n%10
    n=n//10
    re=re*10+r
sqr=re*re
while(sqr>0):
    rem=sqr%10
    sqr=sqr//10
    rev=rev*10+rem
if rev==sq:
    print("True")
else:
    print("False")
n=int(input())
q=n
re=0
while n>0:
    r=n%10
    n=n//10
    re=re*10+r
if(re==q):
    print("True")
else:
    print("False")
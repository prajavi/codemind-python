n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    b=len(str(i))
    if b%2==0:
        c=c+1
print(c)
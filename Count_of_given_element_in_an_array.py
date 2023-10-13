n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
for i in range(0,n):
    if b==a[i]:
        c=c+1
print(c)
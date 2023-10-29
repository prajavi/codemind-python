n=int(input())
a=list(map(int,input().split()))
b=n//2
for i in range(0,n):
    c=a.count(a[i])
    if c>b:
        print(a[i])
        break
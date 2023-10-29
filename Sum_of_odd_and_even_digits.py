n=int(input())
a=list(map(int,input().split()))
s=0
q=0
for i in range(0,n):
    if i%2==0:
        s=s+a[i]
    else:
        q=q+a[i]
if s==q:
    print("YES")
else:
    print("NO")
    
n=int(input())
a=list(map(int,input().split()))
s=0
su=0
for i in range(0,n):
    if i%2==0:
        s=s+a[i]
    else:
        su=su+a[i]
a=s-su
b=su-s
if a>b:
    print(a)
elif b>a:
    print(b)
else:
    print(a)
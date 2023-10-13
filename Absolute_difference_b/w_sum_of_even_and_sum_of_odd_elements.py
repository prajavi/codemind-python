n=int(input())
a=list(map(int,input().split()))
s=0
su=0
for i in a:
    if i%2==0:
        s=s+i
    else:
        su=su+i
a=s-su
b=su-s
if a>b:
    print(a)
elif b>a:
    print(b)
else:
    print(a)
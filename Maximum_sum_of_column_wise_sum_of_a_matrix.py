r,c=map(int,input().split())
s=0
a=[]
b=[]
for i in range(0,r):
    x=list(map(int,input().split()))
    a.append(x)
for v in range(0,c):
    for p in range(0,r):
        s=s+a[p][v]
    b.append(s)
    s=0
print(max(b))
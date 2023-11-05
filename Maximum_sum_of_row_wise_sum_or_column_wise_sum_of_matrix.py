r,c=map(int,input().split())
s=0
su=0
a=[]
b=[]
for i in range(0,r):
    x=list(map(int,input().split()))
    a.append(x)
for v in range(0,r):
    for p in range(0,c):
        s=s+a[v][p]
    b.append(s)
    s=0
for x in range(0,c):
    for y in range(0,r):
        su=su+a[y][x]
    b.append(su)
    su=0
print(max(b))
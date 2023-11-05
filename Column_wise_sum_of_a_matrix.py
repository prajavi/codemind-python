r,c=map(int,input().split())
s=0
x=[]
for i in range(0,r):
    a=list(map(int,input().split()))
    x.append(a)
for p in range(0,c):
    for k in range(0,r):
        s=s+x[k][p]
    print(s,end=' ')
    s=0
    
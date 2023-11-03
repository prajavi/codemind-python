r,c=map(int,input().split())
mat=[]
s=0
q=0
for i in range(0,r):
    a=list(map(int,input().split()))
    mat.append(a)
for p in range(0,r):
    for b in range(0,c):
        if p%2==0:
            s=s+mat[p][b]
        else:
            q=q+mat[p][b]
print(s,q)
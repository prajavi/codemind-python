r=int(input())
mat=[]
mat1=[]
for i in range(0,r):
    a=list(map(int,input().split()))
    mat.append(a)
for j in range(0,r):
    b=list(map(int,input().split()))
    mat1.append(b)
for p in range(0,r):
    for b in range(0,r):
        print(mat[p][b]+mat1[p][b],end=' ')
    print()

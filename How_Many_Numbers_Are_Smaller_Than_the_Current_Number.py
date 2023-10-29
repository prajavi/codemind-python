n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    m=a[i]
    for j in range(0,n):
        if m>a[j]:
            c=c+1
    print(c,end=' ')
    c=0
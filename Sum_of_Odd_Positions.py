n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(1,n,2):
    s=s+a[i]
print(s)
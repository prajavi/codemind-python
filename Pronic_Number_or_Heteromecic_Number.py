n=int(input())
c=0
for i in range(1,n+1):
    p=i*(i+1)
    if p==n:
        c=1
        break
if(c==1):
    print("YES")
else:
    print("NO")
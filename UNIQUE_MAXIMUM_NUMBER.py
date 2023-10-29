n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
for i in a:
    c=a.count(i)
    if c==1:
        b.append(i)
        s=1
if s==1:
    print(max(b))
else:
    print("-1")
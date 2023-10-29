n=int(input())
a=list(map(int,input().split()))
c=0
p=1
q=1
for i in a:
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        p=p*i
    if c!=2:
        q=q*i
    c=0
if p>q:
    print(p-q)
elif q>p:
    print(q-p)
else:
    print(p-q)
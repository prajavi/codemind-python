a,b=map(int,input().split())
for i in range(1,a+1 and b+1):
    if a%i==0 and b%i==0:
        q=[i]
print(max(q))
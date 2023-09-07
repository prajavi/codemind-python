n=int(input())
a=n
c=0
co=0
rev=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if c==2:
    while a:
        r=a%10
        a=a//10
        rev=rev*10+r
    for i in range(1,rev+1):
        if rev%i==0:
            co=co+1
    if co==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
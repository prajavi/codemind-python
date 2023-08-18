a,b,c,d=map(int,input().split())
e=a-b
if (e*c)>(e*d):
    print((b*c)+(e*d))
else:
    print((b*c)+(e*c))
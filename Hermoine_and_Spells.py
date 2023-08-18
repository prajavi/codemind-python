a,b,c=map(int,input().split())
if a>b and a>c:
    if b>c:
        print(a+b)
    else:
        print(a+c)
if b>a and b>c:
    if a>c:
        print(a+b)
    else:
        print(c+b)
if c>a and c>b:
    if a>b:
        print(c+a)
    else:
        print(c+b)
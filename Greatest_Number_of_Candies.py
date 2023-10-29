n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=max(a)
for i in a:
    if (i+b)>=c:
        print("True",end=' ')
    else:
        print("False",end=' ')
    
a=int(input())
b=int(input())
c=0
for i in range(a,b):
    for j in range(1,b):
        if i%j==0:
            c=c+1
    if c==2:
        print(i)
    c=0
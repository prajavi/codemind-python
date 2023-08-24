n=int(input())
c=0
for i in range(1,n+1):
    a=i*i
    if a==n:
        c=1
        break
if c==1:
    print("True")
else:
    print("False")
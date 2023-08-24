s=0
n=int(input())
for i in range(1,n):
    if n%i==0:
        s=s+i
if(s==n):
    print("True")
else:
    print("False")
n=int(input())
a=list(map(int,input().split()))
b=int(input())
flag=0
for i in range(0,n):
    if b==a[i]:
        flag=1
        break
if flag==1:
    print("True")
else:
    print("False")
n=int(input())
li=list(map(int,input().split()))
flag=0
for i in li:
    if i==0 or i==1:
        flag=flag+1
if flag==n:
    print("True")
else:
    print("False")
        
nu=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
s=0
# s=sum(a)
# for i in range(0,nu):
#     if a[i]==m:
#         x=i
# for j in range(0,nu):
#     if a[j]==n:
#         y=j
# z=a[x:y+1]
# p=sum(z)
# print(s-p)
for i in a:
    if i<m or i>n:
        s=s+i
print(s)
w,a,b,c=map(int,input().split())
if w==a or w==b or w==c:
    print("YES")
elif w==(a+b) or w==(b+c) or w==(c+a) or w==(a+b+c):
    print("YES")
else:
    print("NO")
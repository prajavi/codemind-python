a,b,c=map(int,input().split())
s=(a+b+c)/2
b=s*(s-a)*(s-b)*(s-c)
ar=b**0.5
print(f"{ar:.2f}")
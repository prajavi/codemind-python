a=int(input())
if a%5==0 or a%10==0:
    d=a//5
    e=a//10
    print(d-e)
else:
    print("-1")
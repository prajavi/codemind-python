n=int(input())
t=n
s=0
su=0
summ=0
while n:
    r=n%10
    n=n//10
    s=s+r
if s<10 and s>=1:
    print(s)
else:
    while s:
        re=s%10
        s=s//10
        su=su+re
if su<10 and su>=1:
    print(su)
else:
    while su:
        rem=su%10
        su=su//10
        summ=summ+rem
if summ<10 and summ>=1:
    print(summ)

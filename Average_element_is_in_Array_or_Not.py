n=int(input())
a=list(map(int,input().split()))
av=sum(a)//n
print(av in a)
n=int(input())
a=len(str(n))
sq=n*n
b=sq%(10**a)
if b==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
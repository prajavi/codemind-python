bs=float(input())
if bs<=10000:
    da=bs*0.8
    hra=bs*0.2
    gs=(bs+da+hra)
    print(f"{gs:.2f}")
elif bs<=20000:
    da=bs*0.9
    hra=bs*0.25
    gs=(bs+da+hra)
    print(f"{gs:.2f}")
elif bs>20000:
    da=bs*0.95
    hra=bs*0.3
    gs=(bs+da+hra)
    print(f"{gs:.2f}")
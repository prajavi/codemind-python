a=int(input())
if a<=199:
    p=1.20
    bill=1.20*a
    print(f"Units Consumed: {a}")
    print(f"Cost per Unit: {p:.2f}")
    print(f"Bill: {bill:.2f}")
    if bill>400:
        sr=bill*0.15
        tot=bill+sr
        print(f"Surcharge: {sr:.2f}")
        print(f"Total Amount: {tot:.2f}")
    else:
        sr=0
        print(f"Surcharge: {sr:.2f}")
        print(f"Total Amount: {bill:.2f}")
if a>=199 and a<400:
    p=1.40
    bill=1.40*a
    print(f"Units Consumed: {a}")
    print(f"Cost per Unit: {p:.2f}")
    print(f"Bill: {bill:.2f}")
    if bill>400:
        sr=bill*0.15
        tot=bill+sr
        print(f"Surcharge: {sr:.2f}")
        print(f"Total Amount: {tot:.2f}")
    else:
        sr=0
        print(f"Surcharge: {sr:.2f}")
        print(f"Total Amount: {bill:.2f}")
if a>=400 and a<600:
    p=1.60
    bill=1.60*a
    print(f"Units Consumed: {a}")
    print(f"Cost per Unit: {p:.2f}")
    print(f"Bill: {bill:.2f}")
    if bill>400:
        sr=bill*0.15
        tot=bill+sr
        print(f"Surcharge: {sr:.2f}")
        print(f"Total Amount: {tot:.2f}")
    else:
        sr=0
        print(f"Surcharge: {sr:.2f}")
        print(f"Total Amount: {bill:.2f}")
if a>=600 and a<800:
    p=1.80
    bill=1.80*a
    print(f"Units Consumed: {a}")
    print(f"Cost per Unit: {p:.2f}")
    print(f"Bill: {bill:.2f}")
    if bill>400:
        sr=bill*0.15
        tot=bill+sr
        print(f"Surcharge: {sr:.2f}")
        print(f"Total Amount: {tot:.2f}")
    else:
        sr=0
        print(f"Surcharge: {sr:.2f}")
        print(f"Total Amount: {bill:.2f}")
if a>=800:
    p=2.00
    bill=2.00*a
    print(f"Units Consumed: {a}")
    print(f"Cost per Unit: {p:.2f}")
    print(f"Bill: {bill:.2f}")
    if bill>400:
        sr=bill*0.15
        tot=bill+sr
        print(f"Surcharge: {sr:.2f}")
        print(f"Total Amount: {tot:.2f}")
    else:
        sr=0
        print(f"Surcharge: {sr:.2f}")
        print(f"Total Amount: {bill:.2f}")
        
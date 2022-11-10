def factorial(x):
    x=int(x)
    i=1
    c=1
    for i in range(1,x+1):
        c=c*i
        i=i+1
    print(c)
print("Welcome to the world of calculations")
aa=True
while aa==True:
    print("Select one of the following operations")
    print("1-Addition")
    print("2-Subtraction")
    print("3-Multiplation")
    print("4-Division")
    print("5-Exponenentiation")
    print("6-Triginometric Operations")
    print("7-Factorial")
    print("8-Greatest Integer Function")
    print("9-Fractional Part Function")
    print("10-Exit")
    a=int(input("Enter your chosen option(1-10)"))
    if a==1:
        c=float(input("Enter the number"))
        i=1
        while i>0:
            b=input("Enter the number.To see the result, enter end.")
            if b=="end":
                break
            b=float(b)
            c=b+c
            i=i+1
        print("RESULT",c)
    if a==2:
        b=input("Enter first number")    
        c=input("Enter second number.")
        b=float(b)
        c=float(c)
        d=b-c
        print("RESULT",d)
    if a==3:
        c=float(input("Enter the number."))
        i=1
        while i>0:
            b=input("Enter the number.To see the result, enter end.")
            if b=="end":
                break
            b=float(b)
            c=b*c
        print("RESULT",c)
    if a==4:
        b=input("Enter first number.")
        if b=="no":
            print("Welcome to the world of calculations")
            print("Select one of the following operations")
            print("1-Addition")
            print("2-Subtraction")
            print("3-Multiplation")
            print("4-Division")
            print("5-Exponenentiation")
            print("6-Triginometric Operations")
            print("7-Factorial")
            print("8-Greatest Integer Function")
            print("9-Fractinal Part Function")
            print("10-Signum Function")
            a=int(input("Enter your chosen option(1-10)"))    
        c=input("Enter the number")
        b=float(b)
        c=float(c)
        d=float(b/c)
        print("RESULT",d)
    if a==5:
        b=float(input("Enter the base number"))
        c=float(input("Enter the power"))
        d=b**c
        print("RESULT",d)
    if a==6:
        print("Select one of the following options")
        print("1-Sin x")
        print("2-Cos x")
        print("3-Tan x")
        b=int(input("Enter your chosen option(1-3)"))
        if b==1:
            c=float(input("Enter x in radians"))
            d=c-((c**3)/(3*2))+((c**5)/(5*4*3*2))-((c**7)/(7*6*5*4*3*2))+((c**9)/(9*8*7*6*5*4*3*2))-((c**11)/(11*10*9*8*7*6*5*4*3*2))
            print(d)
        if b==2:
            c=float(input("Enter x in radians"))
            d=1-((c**2)/2)+((c**4)/(4*3*2))-((c**6)/(6*5*4*3*2))+((c**8)/(8*7*6*5*4*3*2))-((c**10)/(10*9*8*7*6*5*4*3*2))+((c**12)/(12*11*10*9*8*7*6*5*4*3*2))
            print(d)
        if b==3:
            c=float(input("Enter x in radians"))
            d=c+((c**3)/3)+((2*(c**5))/(15))+((17*(c**7))/(315))+((62*(c**9))/(2835))
            print(d)
    if a==7:
        b=int(input("Enter the number"))
        print("RESULT")
        factorial(b)
    if a==8:
        b=float(input("Enter the number"))
        c=int(b)
        print("RESULT",c)
    if a==9:
        b=float(input("Enter the number"))
        c=int(b)
        print("RESULT",b-c)
    if a==10:
        print("Thank you for visiting")
        aa=False
    

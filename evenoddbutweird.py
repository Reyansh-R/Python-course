def EO(n):
    if (n ^ 1 == n + 1):
        return True
    else:
        return False
    
number = int(input("enter a number: "))

if EO(number):
    print("ITs even")
else:
    print("ITs odd")
    
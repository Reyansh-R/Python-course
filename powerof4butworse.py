n = int(input("Enter a number: "))

def powercheck(n):
    if (n<=0):
        return False
    
    if n == 1:
        return True
    if n%4 == 0:
        return powercheck(n/4)
    return False

if powercheck(n):
    print("Power of 4")
else:
    print("Not power of 4")
    
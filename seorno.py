def SETORNOT(number, n):
    if number & (1 << (n-1)):
        print("set")
    else:
        print("Not set")

number = int(input("Enter a number: "))
n = int(input("Enter bit number: ")) 
SETORNOT(number, n)

def o(number1, number2):
    flips = 0

    while(number1 > 0 or number2 > 0):
        t1 = (number1 & 1)
        t2 = (number2 & 1)
        if (number1 != number2):
            flips += 1
        number1 >>= 1
        number2 >>= 1

    return flips

number1 =  int(input("Enter a number: "))

number2 =  int(input("Enter a number: "))

print("Number of flips needed: ", o(number1, number2))
    
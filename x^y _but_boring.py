def computepower(x, y):
    result = 1
    while(y > 0):
        if (y % 2 == 0):
            x = x * x
            y >>= 1
        else:
            result = result * x
            y = y - 1
    return result
x = int(input("enter a number for x: "))
y = int(input("enter a number for y: "))

print("Total: ", (computepower(x, y)))

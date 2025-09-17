p = int(input("Enter a number: "))
n = int(input("Enter a number: "))

def OT(n):
    iterations = 0
    for i in range(1, n+1):
        iterations += 1
    print("When our number is ", n, "The iterations are", iterations)

OT(n)
OT(p)

print(" With every number, the time taken and iterations will increase")

k = int(input("Enter a number = "))
p = int(input("Enter a number = "))
l = int(input("Enter a number = "))
n = int(input("Enter a number = "))

def OST(n):
    iterations = 0
    for i in range(0, n):
        for j in range(0, n):
            iterations += 1
            print( "*", end = "")
        print("")
    print("When our number is ", n, "Iterations are", iterations)

OST(k)
OST(p)
OST(l)
OST(n)

print(" With every n we take, the time taken is n^2 ")
print("O(n^2)")


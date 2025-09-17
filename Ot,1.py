n = int(input("Enter a number: "))

def printnnumber(n):
    iterations = 0
    print("The number entered by the user is ", n)
    iterations += 1
    print("The total number of iterations is ", iterations, "/n")

printnnumber(10)
printnnumber(20)
printnnumber(n)

print("With any number entered, the time taken by our code won't change")
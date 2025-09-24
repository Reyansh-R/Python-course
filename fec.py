n = int(input("Enter a number that you want to find the factors of= "))

def p_n(n):
    print("The factors of", n,"are: ")
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

p_n(n)


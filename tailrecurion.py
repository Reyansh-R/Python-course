def tailrec(n, num):
    if n > num:
        return
    tailrec(n + 1,num)
    print(n)

n = int(input("Enter a number: "))
tailrec(1, n)
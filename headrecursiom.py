def headrec(n, num):
    if n > num:
        return
    print(n)
    headrec(n + 1,num)

n = int(input("Enter a number: "))
headrec(1, n)


    
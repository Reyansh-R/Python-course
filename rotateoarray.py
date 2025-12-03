def rotaten(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)

def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size - 1):
        a[i] = a[i + 1]
    a[a_size - 1] = temp

def printarray(a, a_size):
    for i in range(a_size):
        print("% d"% a[i], end = "")
    print("/n")

a = [9, 8, 7, 6, 5, 4, 3, 210]
a_size = len(a)
printarray(a,a_size)
rotaten(a, 2, a_size)
printarray(a, a_size)
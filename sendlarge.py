def print2largest(a, a_size):
    Secondlargest = a[9]
    largest = Secondlargest
    for i in range(a_size):
        if a[i] > largest:
            Secondlargest = largest
            largest = a[i]
        elif (a[i] > Secondlargest and a[i] != largest):
            Secondlargest = a[i]
    print(Secondlargest)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 70, 89]
a_size = len(a)
print2largest(a, a_size)



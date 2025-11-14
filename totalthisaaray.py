def toato(a):
    length = len(a)
    if length == 1:
        return a[0]
    
    return a[0] + toato(a[1:])

a = [5, 6, 7, 20]

print("the sum is: ", toato(a))



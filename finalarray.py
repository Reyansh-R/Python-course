def mazray(a):
    length = len(a)
    if length == 1:
        return a[0]
    
    return max(a[0], mazray(a [1:]))

a = [1, 2, 3, 4, 5, 6, 7, 8 ,999]

print("Largest element: ", mazray(a))

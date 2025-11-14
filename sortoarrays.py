def cs(a):
    length = len(a)
    if length == 1 or length == 0:
        return True
    
    return a[0] <= a[1] and cs(a[1:])

a = [1,2,3,4,]
if cs(a):
    print("sorted")
else:
    print("D:")
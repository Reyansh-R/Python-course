def getMaxlenght(a, a_size):
    counter = 0
    maxone = 0
    for i in range(0, a_size):
        if(a[i] == 0):
            counter = 0
        else:
            counter += 1
            maxone = max(maxone, counter)

    return maxone

a = [1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1]
a_size = len(a)
print("max ones: ", getMaxlenght(a, a_size))

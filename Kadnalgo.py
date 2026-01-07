def MSA(a, a_size):
    max = -999999999
    cmax = 0
    for i in range(0, a_size):
        cmax = cmax + a[i]
        if max < cmax:
            max = cmax

        if cmax > 0:
            cmax = 0
    return max

a = [12,2,3,435,43,6,75,68,-9,0]
print(MSA(a, len(a)))


def Kadane(a):
    n = len(a)
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, n):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

def MCS(a):
    n = len(a)
    max_Kadane = Kadane(a)
    max_wrap = 0
    for i in range(0, n):
        max_wrap += a[i]
        a[i] = -a[i]

    max_wrap = max_wrap + Kadane(a)
    if max_wrap > max_Kadane:
        return max_wrap
    else:
        return max_Kadane

a = [12, 2, 3, 12, 34, 124, 1, 3]
print("Maximum circular sum= ", MCS(a))

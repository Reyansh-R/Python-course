import math;

def printpowerset(set, size):
    powersetsize = (int) (math.pow(2, size));
    outer = 0;
    inner = 0;

    for outer in range(0, powersetsize):
        for inner in range(0, size):
            if ((outer & (1 << inner)) > 0):
                print(set[inner], end = "")
        print("")

setsize = int(input("Enter the size of your array: "))

set = []
for i in range(0, setsize):
    n = int(input("Enter element: "))
    set.append(n)

printpowerset(set, len(set))



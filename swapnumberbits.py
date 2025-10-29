def swap1 (a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    print("Swapped: a =", a, "b =", b)

def swap2(a,b):
    a = (a & b) + (a | b)
    b = a + ~(b) + 1
    a = a + ~(b) + 1

    print("Swapped: a = ", a, "b = ", b)

swap1(48,64)
swap2(67,00)

def push0(a, a_size):
    zero = 0
    n = 0
    while(n!=a_size):
        if a[n]!= 0:

            a[n], a[zero] = a[zero], a[n]
            zero+= 1
        n += 1

a =[123, 45, 789, 0, 63, 0, 5235, 0, 0, 47568, 1042390, 0 , 0, 1]
a_size = len(a)
print(a)
push0(a, a_size)
print("array but all the zeroes are at the end: ")
print(a)




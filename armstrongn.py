a = int(input("Enter your number:- "))
d = len(str(a))
rn = 0
temp = a
 
while temp > 0:
    digit = temp % 10
    rn += digit ** d
    temp //= 10 

if a == rn:
    print("Armstrong :D")
else:
    print("D:")

    
a = 10
b = 12
c = 0
if a and b and c:
    print("All the numbers have boolean value as true")
else:
    print("Atleast one number has boolean value as false")

a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

a = 10
b = 12
c = 12
print(a!=b)
print(b!=c)
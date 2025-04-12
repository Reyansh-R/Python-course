M = int(input("Enter your marks in Math = "))
E = int(input("Enter your marks in English = "))
S = int(input("Enter your marks in Science = "))
L = int(input("Enter your marks in second language = "))
G = int(input("Enter your marks in SST = "))

tot = M+E+S+L+G
avg = tot/5
if 91 <= avg <= 100:
    print("Your grade is S")
elif 81 <= avg <= 90:
    print("Your grade is A")
elif 71 <= avg <= 80:
    print("Your grade is B1")
elif 61 <= avg <= 70:
    print("Your grade is B2")
elif 51 <= avg <= 60:
    print("Your grade is C1")
elif 41 <= avg <= 50:
    print("Your grade is C2")
elif 33 <= avg <= 40:
    print("Your grade is D")
elif 21 <= avg <= 32:
    print("Your grade is E1")
elif 0 <= avg <= 20:
    print("Your grade is E2")
else:
    print("Invalid Input")






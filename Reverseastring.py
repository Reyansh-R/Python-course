o = str(input("Enter a string of your choice: "))

str = ('')

for i in o:
    str = i + str
print("the original string = ",o)
print("the reversed string = ",str)
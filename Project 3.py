HM = str(input("Please enter a character : "))

if((HM >= 'a' and HM <= 'z') or (HM >= 'A' and HM <= 'Z')):
    print("The given character ", HM, "is in the alphabet")
else:
    print("The given character ", HM, "is not in the alphabet")
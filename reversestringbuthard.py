def rs(s):
    if len(s) == 1:
        return s[0]
    firstchar = s[0]
    return rs(s[1:]) + firstchar

s = str(input("Enter a phrase: "))
print("Reverse: ", rs(s))


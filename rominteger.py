def romantoint(RomanInput):
    roman = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V': 5, 'I' : 1}
    ri = 0
    for i in range(0, len(RomanInput) - 1):
        if roman[RomanInput[i]] < roman[RomanInput[i + 1]]:
            ri -= roman[RomanInput[i]]
        else:
            ri += roman[RomanInput[i]]
    return ri + roman[RomanInput[-1]]

roman = input("Input roman numeral: ")
print("Integer equivalent:  ", romantoint(roman))    
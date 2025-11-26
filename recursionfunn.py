keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
def pc(combination, curr, output, n):
    if curr == n:
        print(*output, sep=",")
        return
    
    for i in range(len(keypad[combination[curr]])):
        output.append(keypad[combination[curr]][i])

        pc(combination, curr + 1, output, n)
        output.pop()

        if(combination[curr] == 0 or combination[curr] == 1):
            return
        
combination = [2, 9, 6]
n = len(combination)
pc(combination, 0, [], n)


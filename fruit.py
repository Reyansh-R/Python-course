class f:
    taste = 'sweet'
    def __init__(self, name, color):
        self.name = name
        self.color = color
a = f('apple', 'red')
b = f('banana', 'yellow')
g = f('Guava', 'green')
s = f('strawberry', 'red')

print(a.taste)
print(a.name, a.color)
print(b.name, b.color)
print(g.name, g.color)
print(s.name, s.color)

        
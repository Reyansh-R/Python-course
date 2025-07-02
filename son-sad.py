class dad:

    def __init__(self, eyes, aggresive):
        self.eyes = eyes
        self.aggresive = aggresive

    def display(self):
        print("Your eye colour is ",self.eyes)
        print("You are aggresive",self.aggresive)
class son(dad):
    def __init__(self, name, age, eyes, aggresive):
        self.age = age
        self.name = name

        
        super().__init__(eyes, aggresive)
obj = son("Penguin", 8, "Blue", True)
obj.display()

        
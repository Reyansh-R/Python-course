import random
class fq:
    def __init__(self):
        self.fruits = {'apple':'red',
                       'banana':'yellow',
                       'watermelon':'green',
                       'tangerine':'orange',
                       'litchi':'white',
                       'dragonfruit':'magenta',
                       'kiwi':'brown'}
    def q(self):
        while(True):
            fruit, colour = random.choice(list(self.fruits.items()))

            print("What is the colour of {}".format(fruit))
            ua = input()
            if(ua.lower() == colour):
                print("Correct answer")
            else:
                print(":/")

            option = int(input("If u don't want to play enter 0, otherwise enter 1 to play again: "))
            if (option):
                break   
print("welcome to fruit quiz")
f = fq()
f.q()



        
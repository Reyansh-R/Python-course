class c:
    
    
    
    def __mp(self):
        self.self = self

    def __init__(self):
        self.__mp = 120


    def sell(self):
        self.self = self
        print("Selling price: ",format(self.__mp))

    def _smp(self,price):
        self.self = self
        price.self = price
        self.__mp = price

p = c()
p.sell()

p.__mp = 1000
p.sell() 

p._smp(1000)
p.sell




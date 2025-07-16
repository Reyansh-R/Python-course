class Thailand():
    def capital(self):
        print("The capital of Thailand is Bangkok")
    
    def language(self):
        print("The language of Thailand is Thai")
    
    def region(self):
        print("Thailand is located in Eastern Asia")

class Brazil():
    def capital(self):
        print("The capital of Brazil is Rio de Janeiro") 
    
    def language(self):
        print("The language of Brazil is Brazilian Spanish")       

    def region(self):
        print("Brazil is located in South America")

obj_Thailand = Thailand()
obj_Brazil = Brazil()

for country in (obj_Thailand, obj_Brazil):
    country.capital()
    country.language()
    country.region()
        
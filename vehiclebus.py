class V:
    def __init__(self, name, ms, mileage):
        self.name = name
        self.ms = ms
        self.mileage = mileage


class B(V):
    pass

obj = B("volvo bus", 122, 64)
print("vehicle name: ",obj.name,
      "Vehicle max speed: ",obj.ms,
      "Vehicle mileage: ",obj.mileage)




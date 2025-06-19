z1 = [1,2,3,4,5,6,7,8,9]
z2 = [10,11,12,13,14]
z3 = list(zip(z1, z2))
print(z3)

for x, y in zip(z1, z2[::-1]):
    print(x,y)

food = ['rice','chicken','TIDEPOD']
nutrition = ['carb','protein','none']
eat = {food: nutrition for food,
                nutrition in zip(food, nutrition)}
print('/n{}'.format(eat))

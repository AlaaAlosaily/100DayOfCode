import random

x = 3 # int
y = 3.3 # Float
w = 3.3j # Complex
r = 3 + 5j # Complex

print(type(w))
print(type(r))


a = int(y)
print(type(a))

b = complex(y)
print(type(b))
print(b)


rand1 = random.random()
rand2 = random.uniform(1,10)
rand3 = random.randint(1,10)
rand4 = random.randrange(1,10)
Greatings = [ " Hello ", "Hi ", "Hey ", "Howdy ", "Hola "]
rand5 = random.choice(Greatings)
rand6 = random.choices(Greatings, k=10)
arr=[1,2,3,4,5,6,7,8,9]
list1 = list(range(1,100))
rand7 = random.sample(arr, k=3)
rand8 = random.sample(list1, k=3)
print(rand1)
print(rand2)
print(rand3)
print(rand4)
print(rand5 + ", Ala'a ")
print(rand6)
print(rand7)
print(rand8)

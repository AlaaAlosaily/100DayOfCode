import re

x = "apple "
y = "orange "
z = "limon"


basket = x + y + z
print(basket)


w = '123456789'
print(re.findall('..', w))
print(re.findall('...', w))
print(re.findall('.{1,2}', w))
print(re.findall('.{1,4}', w))

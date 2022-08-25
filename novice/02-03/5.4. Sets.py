basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) 
print('orange' in basket) 

print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a) 

print(a - b)

print(a | b)

print(a & b )

print(a ^ b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
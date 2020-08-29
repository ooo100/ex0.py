fruits = ("apple", "banana", "pear")
print(fruits)
print(fruits[-1])
for fruit in fruits:
    print(fruit)
if "strawberry" in fruits:
    print("We don't have strawberry")

fruit = ("apple")
print(type(fruit))
del fruit[0]
print(fruit)
# you can't change anything on tuple
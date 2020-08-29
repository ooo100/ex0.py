fruits = {"apple", "orange", "banana"}
print(fruits)
for x in fruits:
    print(x)
print("apple" in fruits)
fruits.add("mango")
print(fruits)
# set is no ordered
fruits.update(["mango", "strawberry", "watermelon"])
print(fruits)
fruits.discard("orange")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
set1 = ["a", "b", "c"]
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

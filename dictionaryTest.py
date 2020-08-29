cars = [
    "brand": "Tesla",
    "model": "Model X",
    "year": 2020
]
#key and value combination is called dictionary
print(cars)
print(cars["model"])
print(cars.get("model"))
cars["year"] = 2018
print(cars.get("year"))
for item in cars:
    print(item)

for x, y in cars.items():
    print(x,y)
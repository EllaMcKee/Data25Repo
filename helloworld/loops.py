counter = 0

while counter < 10:
    if counter % 2 == 0:
        print("This number {} is even. ".format(counter))
    else:
        print("This number {} is odd. ".format(counter))
    counter += 1

customers = {
    "name": "tess",
    "age": 28
}
basket = ["eggs", "cheese", "bread", "garlic"]

for item in basket:
    print(item)
for customer in customers.values():
    print(customer)

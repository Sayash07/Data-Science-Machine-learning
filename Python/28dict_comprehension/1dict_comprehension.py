products = [
    {"name": "laptop", "price": 100000, "quantity": 10},
    {"name": "phone", "price": 10000, "quantity": 12},
    {"name": "tablet", "price": 10500, "quantity": 14}
]

new = [el["name"] for el in products]
print(new)

new1 = [f"{el['name']} cost is {el['price']}" for el in products]
print(new1)

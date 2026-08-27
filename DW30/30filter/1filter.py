l1 = [5,8,19,21,32]


l2 = list(filter(lambda el:el >= 18, l1))
print(l2)



products = [
    {"name": "laptop", "price": 100000, "quantity": 10},
    {"name": "phone", "price": 10000, "quantity": 12},
    {"name": "tablet", "price": 10500, "quantity": 14}
]


l3 = list(filter(lambda el:el["quantity"] >= 11, products))

print(l3)

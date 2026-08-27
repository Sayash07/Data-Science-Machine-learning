from functools import reduce


# value = reduce(fun,list,initial_value)
# used to find sum/product of all elememts



l1 = [1,2,3,4,5]
l2 = reduce(lambda pre,cur: pre+cur,l1,0)
print(l2)


products = [
    {"name": "laptop", "price": 100000, "quantity": 10},
    {"name": "phone", "price": 10000, "quantity": 12},
    {"name": "tablet", "price": 10500, "quantity": 14}
]

total_price = reduce(lambda pre,cur:pre+cur["price"]*cur["quantity"],products,0)
print(total_price)
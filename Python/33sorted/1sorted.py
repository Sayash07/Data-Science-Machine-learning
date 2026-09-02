students = [
    {"name":"Sayash", "marks": 90},
    {"name":"Nitan", "marks": 70},
    {"name":"Ram", "marks": 80}
]

l3 = sorted(students, key = lambda el:el["marks"])
l4 = sorted(students, key = lambda el:el["marks"], reverse= True)
print(l3)
print(l4)

l5 = sorted (students, key= lambda el:el["name"])
print(l5)
l6 = sorted (students, key = lambda el:len(el["name"]))
print(l6)


str1 = "acb"
output = sorted(str1)
print(output)

# o/p of sorted is always in list
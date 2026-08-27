for el in [1,2,3]:
    print(el)




for el in [1,2,3]:
    print(el * 10)


for el in ["Sayash", "Ram", "Shyam"]:
    print(f"{el} thapa")

for i,el in enumerate([10,20,30]):
    print(i)
    print(el)


for el in (1,2,3):
    print(el)

for el in {1,2,3}:
    print(el)


# for dictionary it should be converted to list

for el in {"name": "Sayash", "age": 25}.keys():
    print(el)

for el in {"name": "Sayash", "age": 25}.values():
    print(el)

for el in {"name": "Sayash", "age": 25}.items():
    print(el)



for el in range(1,11,2):
    print(el)


# stop value is exclusive
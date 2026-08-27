l1 = [10,20,30]

l2 = [el *10 for el in l1]
print(l2)


name = ["Nitan", "Sayash", "Ram"]

Full_name = [ f"({el} Thapa)"for el in name]

print(Full_name)

l3 = ["nitan", "hari"]
l4 = [ el[::-1]for el in l3]
print(l4)


l5 = [ el for el in range(1,11) if el>=5]
print(l5)


l6 = [1,2,3]
l7 = ["even" if el%2==0 else "odd" for el in l6 ]
print(l7)





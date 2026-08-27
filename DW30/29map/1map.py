# map = fun,list



l1= [10,11,12]

def square (el):
 v = el ** 2
 return(v)

l2 = list((map(square,l1)))
print(l2)



l3 = ["Sayash", "Nitan", "Ram"]

def check(el):
 return (f"{el} Thapa")

check()

l4 = map()
# map = fun,list



l1= [10,11,12]

def square (el):
 v = el ** 2
 return(v)

l2 = list((map(square,l1)))
print(l2)



l3 = ["Sayash", "Nitan", "Ram"]

def check(el):
 return f"{el} Thapa"

l4 = list(map(check,l3))
print(l4)

def length(el):
 return len(el)

l5 = list(map(length,l3))
print(l5)

l6 = list(map(lambda el:el+" "+"Thapa" , l3))
print(l6)
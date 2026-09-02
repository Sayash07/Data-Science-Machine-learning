def add(a,b,c):
    print("Hello")
    return (a+b+c)
# return to function call and replace it by return value.

value = add(1,2,3)
print(value)




def add(a,b,c):
    return (a+b+c)
    print("Hello")
# return to function call and replace it by return value.

value = add(1,2,3)
print(value)

"""(This will only print 6, because after return statement, 
 the function will exit and it will not execute any further code in the function.)"""
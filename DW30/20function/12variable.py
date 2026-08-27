# We can store function in variable 

sum = lambda a,b:a+b
print(sum(1,3))



# To store normal function, use below process:


def product (a,b):
    return(a*b)

multiply = product

print(multiply(1,3))


# First class function >> func stored in variable
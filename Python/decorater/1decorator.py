""" 
Decorater is a function
which take one func as input
has one inner function which used inout function
it returns that inner function
 """


def is_Authorized(func):
    def inner():
        print("I am strating wrraper")
        func()
        print("I am ending wrapper")

        return inner



@is_Authorized

def add_product():
   print("I am add product")


add_product()
        
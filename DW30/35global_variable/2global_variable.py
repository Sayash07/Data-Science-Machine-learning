x = 1

def check():
    global x # if global is used, it will not create new variable.
    x = 10
    print(x)

check()

print(x)
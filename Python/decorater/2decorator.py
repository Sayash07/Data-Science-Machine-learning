def is_authorized(fun):
    role = "user"
    def inner(allowed_role):
        if(role in allowed_role):
            fun()
        else:
            print("You are not allowed")
    return inner

@is_authorized
def delete_product():
    print("I will delete product")


@is_authorized
def create_produt():
    print("I will create product")

def read_product():
    print("I will read product")

delete_product(["admin", "superadmin"])
read_product()
create_produt(["user","admin","superadmin"])



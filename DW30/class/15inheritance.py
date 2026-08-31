
class Z:
    z = "Z variable"


class A:
    a = "A variable"
    z = "AZ variable"


class B(A,Z) :
    b = "B variable"


b1 = B()

print(b1.b)
print(b1.a)
print(b1.z)
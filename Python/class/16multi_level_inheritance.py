class GrandFather:
    property1 = "20 ropani field"

class Parent(GrandFather):
    property2 = "10 tola Gold"
    property3 = "20 tola Silver"

class child(Parent):
    pass


obj = child()
print(obj.property1)

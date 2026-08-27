class Student:
    collage_name = "Deerwalk"
    address = "Kathmandu"

    def __init__(self,name,age):
        self.name = "Nitan"
        self.age = 32

obj1 = Student("Nitan", 32)
obj2 = Student("Sayash", 24)

print(obj1.name)
print(obj1.age)
print(obj1.address)

#Obj can access class attribute but class cannot access obj attribute >> print(Student.name)


# Add common attribute to class and diff to obj
# Functions are called methods

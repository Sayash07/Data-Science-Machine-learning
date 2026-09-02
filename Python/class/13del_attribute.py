class Student:
    address = "Kathmandu"

    def __init__(self,name):
        self.name = name


S1 = Student()
print(S1.name)

del(Student.address)
print(Student.address) # It throws an error

        
class Student:
    college_name = "DeerWalk"
    address = "Kathmandu"

    def __init__(self,name, age):
        self.name = name 
        self.age = age
    @classmethod
    def change_address(cls):
        cls.address = "Sifal"

    @classmethod
    def get_address(cls):
        print (cls.address)

    @classmethod
    def change_college_name(cls):
        cls.college_name = "Deerwalk Compare"

    @classmethod
    def get_college_name(cls):
        print(cls.college_name)
    


obj1 = Student("Nitan", 32)

obj1.change_address()
obj1.get_address()
obj1.change_college_name()
obj1.get_college_name()


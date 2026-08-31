class Student:
    college_name = "Deerwalk"
    address = "Kathmandu"

    @classmethod
    def change_address(cls, name):
        cls.name = name
    @classmethod
    def get_address(cls):
        print(cls.address)
        


S1 = Student()
S1.change_address("Sifal")
S1.get_address()

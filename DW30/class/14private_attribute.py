class Student:
    __college_name = "Deerwalk"

    @classmethod
    def get_college_name(cls):
        print(cls.__college_name)

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.__password = password


S1 = Student("nitan", "Nitan@gmail.com", "abc@123")
S1.get_college_name()
print(S1.name)
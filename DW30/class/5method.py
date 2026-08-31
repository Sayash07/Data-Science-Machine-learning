class Student:
    college_name = "Deerwalk"
    address = "Kathmandu"

    def __init__(self):
        print("I'm a constructor")

    def getTeacher(self):
        print("I will show you teacher list")

    def addTeacher(self):
        print("I will add teacher")

obj1 = Student()
#Get method using object
obj1.getTeacher()
obj1.addTeacher()

#Get method using class
Student.getTeacher(obj1)

""" 
Object variable >> It can control obj variable
Static Variable >> It cannot control variable
Class variable >>It can control class variable"""


              
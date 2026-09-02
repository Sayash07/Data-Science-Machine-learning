class Student:
    school_name = "Deerwalk"
    address ="Kathmandu"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        avg = sum(self.marks)/len(self.marks)
        print(f"{self.name} average is {avg}")

    def percentage(self):
        percent = (sum(self.marks)/(len(self.marks)*100))*100
        print(f"{self.name} percentage is {percent}%")

    @classmethod
    def change_adress(cls):
        cls.address = "Sifal"
    @classmethod
    def get_address(cls):
        print(cls.address)




S1 = Student("Sayash", [100, 100, 100])
S2 = Student("Nitan", [10, 100, 10])


S1.average()
S2.average()
S1.percentage()
S2.percentage()
S1.change_adress()
S1.get_address()

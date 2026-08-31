class GrandFather:
    def __init__(self):
         print("I'm Grandfather")

class Parent(GrandFather):
    def __init__(self):
            print("I'm parent")
            super().__init__()

class child(Parent):
    def __init__(self):
        print("I'm child")
        super().__init__()


obj = child()

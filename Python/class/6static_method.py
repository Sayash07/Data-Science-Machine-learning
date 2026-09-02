#static method > method which doesn;t have access to both class and obj attributes.

class Students:
    def __init__(self, name):
        self.name= name

    @staticmethod
    def check():
        print("I'm static method.")


S1 = Students("Sayash")
S1.check()

    
        
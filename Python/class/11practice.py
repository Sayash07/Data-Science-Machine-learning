class Linear_Regression:

    def __init__(self,m,c):
        self.m = m
        self.c = c

    def predict(self,x):
        y = self.m * x + self.c
        print(y)


Module = Linear_Regression(1,2)
Module.predict(10)
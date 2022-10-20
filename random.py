class A:
    @staticmethod
    def hi():
        print("Hi, how are you ?")

    def __init__(self):
        print("This is from class A constructor ... ")
        super().__init__()

    def hello(self):
        print("This is from class A's 'hello' method ... ")

class D:
    def __init__(self):
        print("This is from class D's constructor ..")
        super().__init__()


class B(A,D):
    def __init__(self):
        print("This is from class B constructor ... ")
        super().__init__()


obj = B()
obj.hi()
print(A.mro())
print(B.mro())
print(D.mro())


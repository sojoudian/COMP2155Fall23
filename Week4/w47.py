# dunder = double underscore method __init__

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_yourself(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old")    
    

instance1 = Person("Maz", 35)
instance2 = Person("John", 21)

instance1.introduce_yourself()
instance2.introduce_yourself()
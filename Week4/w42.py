
class Person:
    #this is to define a class for a person
    def __init__(self, name, age): #dunder doule underscore
        self.full_name = name
        self.age = age
    def get_age(self):
        print(self.age)
        return self.age
    
maz = Person("Maz", 35)
name = maz.get_age
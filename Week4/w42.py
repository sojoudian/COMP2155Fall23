
class Person:
    #this is to define a class for a person
    def __init__(self, name, age): #dunder doule underscore
        self.full_name = name
        self.age = age
    def get_age(self):
        return self.age

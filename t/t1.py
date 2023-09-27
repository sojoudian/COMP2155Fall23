class Student:
    #“““A class representing a student ”””
    def __init__(self,n,a):
        self.full_name = n
        self.age = a
    def get_age(self):
        return self.age


f = Student("Bob Smith", 23)
print(f.full_name)
print(f.get_age())

print(getattr(f, "full_name"))
print(getattr(f, "get_age"))
#print(getattr(f, "get_birthday"))
class Student:
    def __init__(self, name, age, studentID):
        self.name = name
        self.age = age
        self.studentID = studentID
    def get_sID(self):
        return self.studentID
    
zeb = Student("Zebang", 26, 101406583)
#Access the attribute:
print(zeb.name)
print(zeb.age)

#Access the method of the classa
zeb.get_sID()

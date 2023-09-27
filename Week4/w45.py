class Student:
    def __init__(self, name, age, studentID):
        self.name = name
        self.age = age
        self.studentID = studentID
    def get_sID(self):
        return self.studentID
    
s = Student("Maz", 35, 500112233)
a = Student("John", 22, 500222100)
#Access the attribute:
print(s.name)
print(a.name, a.age)

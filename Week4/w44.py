class Student:
    def __init__(self, name, age, studentID):
        self.name = name
        self.age = age
        self.studentID = studentID
    def get_sID(self):
        return self.studentID


s = Student("Zeb", 26, 101406583)
#Access the attribute:
print(s.name)

#Access the method of the classa
s.get_sID()

getattr(s, "get_sID")
#getattr(s, "get_Student_Course")

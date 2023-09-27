class Teacher:
    #“A class representing teachers.”
    def __init__(self, n):
        self.full_name = n
    def print_name(self):
        print(self.full_name)

m = Teacher("Maz")

print(m.full_name)
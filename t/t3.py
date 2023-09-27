class counter:
    overall_total = 0       #class attribute
    def __init__(self):
        self.my_total = 0   #data attribute
    def increment(self):
        counter.overall_total = \
        counter.overall_total + 1
        self.my_total = \
        self.my_total + 1

a = counter()        
b = counter()

a.increment()
b.increment()
b.increment()

print("a.my_total:", a.my_total)
print("counter.overall_total:", counter.overall_total)


print("b.my_total:", b.my_total)
print("counter.overall_total:", counter.overall_total)
class Circle:
    def __init__(self, radius):
        self.radius = radius
    # getter for radius    
    @property
    def radius(self):
        print("Hi from Radius method")
        return self._radius
    
    #setter
    @radius.setter
    def radius(self, value):
        if value < 0:
            print("Radius cannot be negative!")
        else:
            print("Setting radius")
            self._radius = value

    # a public method to calculate the area of the Circle
    def area(self):
        import math
        return math.pi * self._radius ** 2
    

c = Circle(5)
print(c.radius)

#setting the radius using attributes sets by a setter
c.radius=7

#c.radius=-3
print(c.area())
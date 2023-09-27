class Circle:
    def __init__(self, radius):
        self._radius = radius  # _radius is intended to be a protected attribute
    
    # Getter for radius
    @property
    def radius(self):
        print("Getting radius")
        return self._radius
    
    # Setter for radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            print("Radius cannot be negative!")
        else:
            print("Setting radius")
            self._radius = value
    
    # Method to calculate the area of the circle
    def area(self):
        import math
        return math.pi * self._radius ** 2

# Create an instance of the Circle class
circle = Circle(5)

# Accessing the radius attribute using the getter
print("Accessing the radius attribute using the getter")
print(circle.radius)  # Output: Getting radius
                      #         5

# Setting the radius attribute using the setter
circle.radius = 7     # Output: Setting radius

# Trying to set the radius to a negative value
circle.radius = -3    # Output: Radius cannot be negative!

# Calculate and print the area of the circle
print(circle.area())  # Output: 153.93804002589985

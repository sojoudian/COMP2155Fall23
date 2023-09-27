class Dog:
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says hi!")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Charlie", "Beagle")

print(Dog.species)

print(dog1.species)
print(dog2.species)

print(dog1.name, dog1.breed)
print(dog2.name, dog2.breed)

dog1.bark()
dog2.bark()
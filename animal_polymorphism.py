# Defined the base Animal class
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Defined subclasses
class Dog(Animal):
    def move(self):
        print("The dog is running! 🐕")

class Cat(Animal):
    def move(self):
        print("The cat is sneaking around! 🐱")

class Bird(Animal):
    def move(self):
        print("The bird is flying high! 🦅")

# Polymorphism in action
if __name__ == "__main__":
    animals = [Dog(), Cat(), Bird()]

    # Loop through each animal and call its move() method
    for animal in animals:
        animal.move() 

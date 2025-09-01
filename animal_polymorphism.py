# Define the base Animal class
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Define subclasses that override the move method
class Dog(Animal):
    def move(self):
        print("The dog is running! 🐕")

class Cat(Animal):
    def move(self):
        print("The cat is sneaking around! 🐱")

class Bird(Animal):
    def move(self):
        print("The bird is flying high! 🦅")

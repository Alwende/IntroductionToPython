class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("The dog is running.")

class Bird(Animal):
    def move(self):
        print("The bird is flying.")

class Fish(Animal):
    def move(self):
        print("The fish is swimming.")

# Example usage
if __name__ == "__main__":
    animals = [Dog(), Bird(), Fish()]

    for animal in animals:
        animal.move()
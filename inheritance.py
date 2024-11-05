class Animal:
    def eat(self):
        print("The animal is eating.")

    def sleep(self):
        print("The animal is sleeping.")

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

# Demonstration
dog = Dog()
dog.eat()
dog.sleep()
dog.bark()

class Cat:
    def make_sound(self):
        print("Meow")

class Dog:
    def make_sound(self):
        print("Woof woof")

def animal_sound(animal):
    animal.make_sound()


cat = Cat()
dog = Dog()
animal_sound(cat)
animal_sound(dog)

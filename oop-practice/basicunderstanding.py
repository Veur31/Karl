class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def sound(self):
            print(f"This is the sound dog: {self.name}")
class Cat(Animal):
    def sound(self):
            print(f"This is the sound of cat: {self.name}")
def animal_sound(animal):
     animal.sound()
     
dog = Dog("Arf Arf")
cat = Cat("Meow Meow")

animal_sound(dog)
animal_sound(cat)


        
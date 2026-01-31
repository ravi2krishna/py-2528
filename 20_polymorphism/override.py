# Method Overriding 

class Animal:
    def sound(self):
        print("Animal Makes Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Makes Sound - Woof")

class Cat(Animal):
    def sound(self):
        print("Cat Makes Sound - Meow")
        
class Cow(Animal):
    def sound(self):
        super().sound()
        print("Cow Makes Sound - Mooo")
        
animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

cow = Cow()
cow.sound()
# Types Of Inheritance

class Father:
    def house(self):
        print("Has House")

class Son: # No Inheritance
    def car(self):
        print("Has Car")
        
son_obj = Son()
son_obj.car()
# son_obj.house() # AttributeError: 'Son' object has no attribute 'house'

print("=" * 20)

# With Inheritance

# Single Level Inheritance: One Parent -> One Child 
class Father:
    def house(self):
        print("Has House")

class Son(Father): # With Inheritance
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.car()
son_obj.house()

print("=" * 20)

# Multi Level Inheritance: GrandParent -> Parent -> Child 

class GrandFather():
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")

class Son(Father): # With Inheritance
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.car()
son_obj.house()
son_obj.land()

print("=" * 20)

# Multiple Inheritance: One Child -> Multiple Parents 

class GrandFather():
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")

class Mother:
    def gold(self):
        print("Has Gold")

class Son(Father,Mother): # Multiple Inheritance
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.car()
son_obj.house()
son_obj.land()
son_obj.gold()

print("=" * 20)

# Hierarchial Inheritance: One Parent -> Multiple Childs
class Father:
    def house(self):
        print("Has House")

class Son(Father): # With Inheritance
    def car(self):
        print("Has Car")

class Daughter(Father): # With Inheritance
    def business(self):
        print("Has Business")

son_obj = Son()
son_obj.car()
son_obj.house()

daughter_obj = Daughter()
daughter_obj.business()
daughter_obj.house()

print("=" * 20)

# Hybrid Inheritance: Combination Of two or more types 
class A:
    def a(self):
        print("A")

class B(A):
    def b(self):
        print("B")

class C(A):
    def c(self):
        print("C")

class D(B,C):
    def d(self):
        print("D")

obj_d = D()
obj_d.a()
obj_d.b()
obj_d.c()
obj_d.d()
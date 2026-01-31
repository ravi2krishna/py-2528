# Method Overloading
# define multiple methods with the same name but different parameter lists 

class MathOps:
    
    def add(self,a,b):
        return a + b 
    
    def add(self,a,b,c):
        return a + b +c 

obj = MathOps()
# print(obj.add(10,20)) # TypeError: MathOps.add() missing 1 required positional argument: 'c'
print(obj.add(10,20,30))
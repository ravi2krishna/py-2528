# Private 

class A:
    def __init__(self,a,b):
        self.__a = a # private
        self.__b = b # private

obj = A(10,20)
print(obj.a) # Accessible 
print(obj.b) # Accessible 
# print(obj._MyClass__private_variable)
# print(obj._A__a) # You shouldn’t, but you can if you insist.

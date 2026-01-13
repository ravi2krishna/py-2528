# Functional Style Programming 

# Without Functions

a = 10
b = 5

# Math Operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 50)

a = 20
b = 5

# Math Operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 50)

a = 200
b = 100

# Math Operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 50)

# With Functions 
def math_ops():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

a = 10
b = 5
math_ops()
print("=" * 50)
a = 20
b = 5
math_ops()
print("=" * 50)
a = 200
b = 100
math_ops()
print("=" * 50)

# Using Functions With Parameters 
def math_ops(a,b): # a & b are Parameters
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'a' and 'b'
math_ops(10,5) # 10 and 5 are Arguments 
print("=" * 50)
math_ops(20,5)
print("=" * 50)
math_ops(200,100)
print("=" * 50)

# Positional Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")
    
employee_info("hyderabad","ravi","ravi@gmail.com")
employee_info("ravi","ravi@gmail.com","hyderabad")
# employee_info("ravi","ravi@gmail.com") # TypeError: employee_info() missing 1 required positional argument: 'emp_location'

# Keywords Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")
    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")

# No Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
# employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com") # TypeError: employee_info() missing 1 required positional argument: 'org_name'
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com",org_name="Google")
employee_info(emp_location="new york",emp_name="john",emp_email="john@gmail.com",org_name="Google")
employee_info(emp_location="pune",emp_name="sai",emp_email="sai@gmail.com",org_name="Google")

# With Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")
employee_info(emp_location="new york",emp_name="john",emp_email="john@gmail.com")
employee_info(emp_location="pune",emp_name="sai",emp_email="sai@gmail.com")
employee_info(emp_location="bangalore",emp_name="mike",emp_email="mike@gmail.com",org_name="META")

# With Default Arguments Wrong Placement
# def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile): # Non-default argument follows default argument
#     print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")

# With Default Arguments Correct Placement
def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile="999"): 
     print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
     
# Arbitrary Positional Arguments

# def add_numbers(a)     
# def add_numbers(a,b)
# def add_numbers(a,b,c,d,e)

# def add_numbers(*a)

def add_numbers(*nums):
    print(nums)

add_numbers(10)
add_numbers(10,20)
add_numbers(10,20,30,40,50)

def add_numbers(*nums):
    total = 0
    for num in nums:
        total = total + num 
    print(f"Total Sum is: {total}")

add_numbers(10)
add_numbers(10,20)
add_numbers(10,20,30,40,50)

# Arbitrary Keyword Arguments

# def add_numbers(a=10)     
# def add_numbers(a=10,b=20)

# def add_numbers(**a)

def profile(**info):
    print(info)

profile(fname="ravi")
profile(fname="ravi",lname="krishna")

def bank_transactions(**trans):
    print(trans)
    total = 0
    for transaction in trans:
        total = total + trans[transaction]
    print(f"You have done done transactions which totals to {total} ")

bank_transactions(jan=1000,feb=2500,mar=3500)
bank_transactions(jan=1000,feb=2500,mar=3500,apr=5000,may=7000,june=9000)
        
print("=" * 50)

# Without return 
def add(a,b):
    a + b 

add(10,20)
print(add(10,20)) # Without return, by default a function returns None 

# With return 
def add(a,b):
    return a + b 

add(10,20)
print(add(10,20))

# Function Composition 
def sub(c,d,e): # add c + d then minus e i.e finally c + d - e
    return add(c,d) - e 
print(sub(3,4,5)) # 2

# return should be last part of statement to be executed
def add(a,b):
    return a + b 
    print("Calculation Done") # Code is structurally unreachable
    
print(add(10,20))

# multiple return statements, first will be considered
def add(a,b):
    return a + b 
    return a - b # Code is structurally unreachable
    return a * b # Code is structurally unreachable

print(add(10,20))

# multiple return statements, valid with correct conditions 
def math_ops(a,b,opr):
    if opr == "+":
        return a + b
    elif opr == "-":
        return a - b
    elif opr == "*":
        return a * b
    elif opr == "/":
        return a / b
    else:
        return "Invalid Operator"

print(math_ops(10,5,"+"))
print(math_ops(10,5,"*"))
print(math_ops(10,5,"$"))

# Local scope i.e local variables
def add():
    la = 10 # local variable
    lb = 20 # local variable
    print(la) # accessed within function
    print(lb) # accessed within function

add()
# print(la) # accessed local variable outside function # NameError: name 'la' is not defined. Did you mean: 'a'?
    
# Local scope i.e local variables
def add(la,lb): # la & lb are local variable
    print(la) # accessed within function
    print(lb) # accessed within function

add(30,40)
# print(la) # accessed local variable outside function # NameError: name 'la' is not defined. Did you mean: 'a'?

# Global Scope i.e global variables
ga = 100 # global variable
def add(la,lb): # la & lb are local variable
    print(la) # accessed within function
    print(lb) # accessed within function
    print(ga) # global variable accessed within function

print(add(80,90))
print(ga)

# Name Conflict Scenario
ga = 100 # global variable
def add(la,lb,ga): # la, lb & ga are local variable
    print(la) # accessed within function
    print(lb) # accessed within function
    print(ga) # local variable accessed within function, as per preference
    print(globals()['ga']) # global variable accessed within function, using globals()
    
print(add(40,50,60)) # 40, 50, 60, 100

# Global Variable Outside function  
count = 0
print(count)
count += 1
print(count)

# Global Variable inside function  
count = 0
def increment():
    global count
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    return count
print(increment())

# Built In Functions 
# id(), type(), dir(), input(), len(), max(), min()
data = [10,20,30,40,50]
print(id(data))
print(type(data))
print(dir(data))
print(len(data))
print(max(data))
print(min(data))

# print(dir(__builtins__)) # checking built in 

# User Defined Functions i.e Without Lambda 
def add(a,b):
    return a+b
print(add(20,30))

# With Lambda
# syntax -> lambda arguments:expression
# lambda a,b:a+b
print((lambda a,b:a+b)(100,200))    

# Without Lambda 
def is_even_num(num):
    if num % 2 == 0:
        return True 
    else:
        return False
print(is_even_num(10))
print(is_even_num(5))

# With Lambda 
print((lambda num:num % 2 == 0)(100))  
print((lambda num:num % 2 == 0)(95))

# Without Lambda 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")
    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")

# With Lambda 
print((lambda emp_name,emp_email,emp_location:print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}"))(emp_location="new york",emp_name="john",emp_email="john@gmail.com"))  

# Without map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5] ==> [1,4,9,16,25]
def square_list(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num * num)
    return squared_list

print(square_list([1,2,3,4,5]))

# With map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5] ==> [1,4,9,16,25]
# syntax -> map(function, iterable)
# syntax -> lambda arguments:expression 
print((lambda num: num*num))
# print(map(function,[1,2,3,4,5]))
print(map((lambda num: num*num),[1,2,3,4,5]))
print(list(map((lambda num: num*num),[1,2,3,4,5])))

# Real World Use Case Of Working With Lambda & Higher Order Functions 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},
]
# find me prices after discount 
prices_after_discount = []
for product in products:
    price = product["price"]
    discount = product["discount"]
    
    price_after_discount = price - (price * discount / 100)
    prices_after_discount.append(price_after_discount)

print(prices_after_discount)

# Real World Use Case Of Working With Lambda & Higher Order Functions 
# syntax -> map(function, iterable)
# syntax -> lambda arguments:expression 
# lambda product: product["price"] - product["price"] * product["discount"] / 100
# lambda p: p["price"] - p["price"] * p["discount"] / 100
# print(map(function,[1,2,3,4,5]))
print(list(map((lambda p: p["price"] - p["price"] * p["discount"] / 100),products)))

# without filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10] ==> [2,4,6,8,10]
def even_list(numbers):
    evened_list = []
    for num in numbers:
        if num % 2 == 0:
            evened_list.append(num)
    return evened_list

print(even_list([1,2,3,4,5,6,7,8,9,10]))

# With filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10] ==> [2,4,6,8,10]
# syntax -> filter(function, iterable)
# syntax -> lambda arguments:expression 
print((lambda num: num % 2 == 0))
# print(map(function,[1,2,3,4,5]))
print(filter((lambda num: num % 2 == 0),[1,2,3,4,5,6,7,8,9,10]))
print(list(filter((lambda num: num % 2 == 0),[1,2,3,4,5,6,7,8,9,10])))


# Real World Use Case Of Working With Lambda & Higher Order Functions 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},
]
# find me premium products i.e a product with price above 25000 
premium_products = []
for product in products:
    price = product["price"]
    if price > 25000:
        premium_products.append(product)

print(premium_products)

print(list(filter((lambda p: p["price"] > 25000),products)))

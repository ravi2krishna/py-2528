# Conditional Structures / Statements (Decision Making Statements)

# if condition
if 1 > 0: # below block of code executes, only when the condition is True 
    print("block")
    print("of")
    print("code")
    print("executed")
    
if -1 > 0: # below block of code executes, only when the condition is True 
    print("new")
    print("code")
    print("executed or not")
    
num = 5
if num > 0:
    print("Given Number Is Positive")
if num < 0:
    print("Given Number Is Negative") 


# if else condition
num = -5
if num > 0: # below block of code executes, only when the condition is True 
    print("Given Number Is Positive")
else: # below block of code executes, only when the condition is False 
    print("Given Number Is Negative") 
    
# if else condition
num = 0
if num > 0: # below block of code executes, only when the condition is True 
    print("Given Number Is Positive")
else: # below block of code executes, only when the condition is False 
    print("Given Number Is Negative")
if num == 0:
    print("Given Number Is Zero")

# input(): reads input from user 
name = input("Enter Your Name: ")
print(name)

# Interpolation replaces, place holders with actual values dynamically
print('Welcome: name')
print('Welcome: {name}')
print(f'Welcome: {name}')

# Simple Calculator 
num1 = input("Enter Number One: ")
num2 = input("Enter Number Two: ")
sum = num1 + num2 
print(f'Sum Of Numbers is {sum}')

# Simple Calculator 
num1 = input("Enter Number One: ")
num2 = input("Enter Number Two: ")
num1 = int(num1) # type casting
num2 = int(num2) # type casting
sum = num1 + num2 
print(f'Sum Of Numbers is {sum}')

# Simple Calculator 
num1 = int(input("Enter Number One: ")) # type casting
num2 = int(input("Enter Number Two: ")) # type casting
sum = num1 + num2 
print(f'Sum Of Numbers is {sum}')

# Voting App 
age = 20
if age >= 18:
    print("You Can Vote")
else:
    print("You Cannot Vote")
    
# Voting App - Dynamic     
age = int(input("Enter Your Age: "))
if age >= 18:
    print("You Can Vote")
else:
    print("You Cannot Vote")

# ternary operator / "conditional expression"
# value_if_true if condition else value_if_false     
age = int(input("Enter Your Age: "))
status = "You Can Vote" if age >= 18 else "You Cannot Vote"
print(status)
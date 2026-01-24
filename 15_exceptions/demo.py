# Exception Handling

# When There is No Error -> Nothing To Handle 
print("Program Execution Started")
num1 = 10
num2 = 5
print(num1/num2)
print("Program Execution Completed")

print("=" * 50)

# When There is Error -> Python Handles by abruptly "STOPPING" the program execution
print("Program Execution Started")
num1 = 10
num2 = 0
# num2 = "5"
# print(num1/num2) # ZeroDivisionError: division by zero
print("Program Execution Completed")

print("=" * 50)

# When There is Error -> User can handle by try & except with some meaningful info 
print("Program Execution Started")
num1 = 10
num2 = 0
# num2 = "5"
# print(num1/num2) # ZeroDivisionError: division by zero
try:
    print(num1/num2)
except:
    print("OOPS! We Got An Error - Check Below Link For Info")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")

print("=" * 50)

# When We Have Multiple Errors 
print("Program Execution Started")
# data = [1,2,'python',0,5] # TypeError: unsupported operand type(s) for /: 'int' and 'str'
# data = [1,2,0,5] # ZeroDivisionError: division by zero
data = [1,2,5]
for num in data:
    print(1/num)
print("Program Execution Completed")
print("=" * 50)

# When We Have Multiple Errors -> Exception Handling 
print("Program Execution Started")
data = [1,2,'python',0,5] 
for num in data:
    try:
        print(1/num)
    except:
        print("OOPS! Something Went Error")
print("Program Execution Completed")
print("=" * 50)

# We got same message for all errors 

# When We Have Multiple Errors -> Exception Handling 
print("Program Execution Started")
data = [1,2,'python',0,5] 
for num in data:
    try:
        print(1/num)
    except TypeError:
        print("OOPS! You Should Not Divide Number With String")
    except ZeroDivisionError:
        print("OOPS! You Should Not Divide Number With Zero")
print("Program Execution Completed")
print("=" * 50)
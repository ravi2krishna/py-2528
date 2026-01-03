# Set Methods / Operations 

# add(): add element to set
data = {10,20,30,40,50}
print(data)
data.add(60)
print(data)

# update(): add multiple elements to set
data = {10,20,30,40,50}
print(data)
data.update([60,70,80])
print(data)

# pop(): removes random element
data = {10,20,30,40,50}
print(data)
data.pop()
print(data)

# remove(): removes element by value
data = {10,20,30,40,50}
print(data)
data.remove(20)
# data.remove(200) # KeyError: 200
print(data)

# discard(): removes element by value, if value doesn't exist, no error
data = {10,20,30,40,50}
print(data)
data.discard(20)
data.discard(200)
print(data)

# clear(): removes all elements and empties 
data = {10,20,30,40,50}
print(data)
data.clear()
print(data)

# copy(): makes a new copy
data = {10,20,30,40,50}
print(data)
backup = data.copy()
print(backup)

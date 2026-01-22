# Working With JSON Files

student = {
    "id": 101,
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","django","react"],
    "gpa": 9.5
}

print(type(student))
print(student)

# Write Data To JSON File 
import json
with open("14_file_manage/student.json","w") as file_data:
    # json.dump(student) # TypeError: dump() missing 1 required positional argument: 'fp'
    json.dump(student,file_data)
    
# Write Data To JSON File With Indentation
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)

# Read Data From JSON File 
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)
    print(type(data))

# Requirement: Get Student Name & Number Of Courses he joined from student.json 
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
print("Student Name: ", data['name'])
print("Number Of Courses Enrolled: ", len(data['courses']))

# Requirement: Check If Student is passed or not based on gpa above 7
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    
if data['gpa'] > 7:
    print("Passed")
else:
    print("Failed")
    
# File based -> dump() & load()

# Python Object based -> dumps() & loads()

student = {
    "id": 101,
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","django","react"],
    "gpa": 9.5
}

print(type(student))
print(student)

json_data = json.dumps(student)
print(type(json_data))
print(json_data)

string_data = '{"id": 101, "name": "Ravi", "email": "ravi2krishna@gmail.com", "courses": ["python", "django", "react"], "gpa": 9.5}'
print(type(string_data))
dict_data = json.loads(string_data)
print(type(dict_data))

# Building Full Stack Python Application (API) - JSON Use Case
import urllib.request
api_url = 'https://dummyjson.com/users'

response = urllib.request.urlopen(api_url)
print(response)

# Read Content 
api_data = response.read()
print(api_data)
print(type(api_data))

# Convert Data 
api_data = json.loads(api_data)
print(api_data)
print(type(api_data))

# Customer Requirement: List Me Users & Count Users 
users = api_data['users']
print(users)
print(type(users))
print("Number Of Users: ",len(users))

# individual user data with age
for user in users:
    print(user['username'], user['age'] )
    
# Customer Requirement: List Me Users Below Age 30
print("======== Young Employees ========")
for user in users:
    if user['age'] < 30:
        print(user['username'], user['age'] )
# Student Management System With Persistent Storage

# menu based system ==> in future replace with UI elements like buttons 

# System Setup Info On Start up
SYSTEM_INFO = ("Edify Technologies","Student Management System","v1")

# Admin Info at end
ADMIN_INFO = ("9090880","admin@edify.com")

# File To Store student data 
FILE_NAME = "14_file_manage/students.json"

# Importing Appropriate Modules
import os 
import json

# loading students data from json file 
def load_students():
    # Read Data From JSON File
    with open(FILE_NAME,"r") as file_data:
        return json.load(file_data)
    
# save students data to json file 
def save_students():
    
    with open(FILE_NAME,"w") as file:
        json.dump(students,file,indent=4)
        # TypeError: Object of type set is not JSON serializable
             
# set student details in dictionary 
students = load_students()

# Start Up Info
print("="*50)
print(f"Welcome To {SYSTEM_INFO[0]}")
print(f"Software Name {SYSTEM_INFO[1]} {SYSTEM_INFO[2]}")
print("="*50)

# adding student function
def add_student():
        print("Adding Student")
        
        student_id = input("Enter ID: ")
        if student_id in students:
            print("Student already exists")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <= 100:
                        scores.append(score)
                    else:
                        print("Score should be (0-100)")
                else:
                    print("Invalid Score, only digits allowed")
                    
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input)
            
            # save student details to dictionary
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            
            print("Student Added")
            save_students()
            print(students) # for confirmation i.e test

# updating student function
def update_student():
        print("Updating Student")
        student_id = input("Enter ID: ")
        if student_id in students:
            new_name = input("Enter New Name: ").title()
            students[student_id]["name"] = new_name
            # students[student_id] = {"name":new_name}
            print("Student Updated")
            
        else:
            print("Student doesn't exists")
        save_students()
        print(students) # for confirmation i.e test

# deleting student function
def delete_student():
        print("Deleting Student")
        student_id = input("Enter ID: ")
        if student_id in students:
            remove_student = students.pop(student_id)
            print(remove_student)
            save_students()
        else:
            print("Student doesn't exists")
            
        print(students) # for confirmation i.e test

# listing student function
def list_student():
        print("Listing Student")
        # {'101': {'name': 'John', 'scores': [90], 'skills': {'git'}}, 
        # '102': {'name': 'Mike', 'scores': [90], 'skills': {'python'}}}
        for sid, data in students.items():
            name = data['name']
            scores = data['scores']
            avg_score = sum(scores) / len(scores)
            high_score = max(scores)
            least_score = min(scores)
            skills = data['skills']
            skills_count = len(skills)
            
            print(f"ID: {sid}")
            print(f"Name: {name}")
            print(f"All Scores: {scores}")
            print(f"Average Score: {avg_score}")
            print(f"Maximum Score: {high_score}")
            print(f"Least Score: {least_score}")
            print(f"All Skills: {skills}")
            print(f"Skills Count: {skills_count}")

# exist application
def exist_system():  
        print("Exiting Application")
        print("="*50)
        print(f"Contact Admin : {ADMIN_INFO[0]}")
        print(f"Email Admin: {ADMIN_INFO[1]}")
        print("="*50)  
    
# search by skill 
def search_student_skill():
    skill_to_search = input("Enter Skill & Search: ")
    filtered_students = filter(lambda s: skill_to_search in students[s]['skills'] ,students)
    
    if filtered_students:
        print(f"Students With Skills {skill_to_search}")
        for sid in filtered_students:
            print(f"ID: {sid}   |   Name: {students[sid]['name']}")
    else:
        print(f"No Students Found With Skills {skill_to_search}")
        
    
# menu based system
while True:
    print("Choose An Option: ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - List Student")
    print("5 - Search By Skill")
    print("6 - Exit Application")
    
    choice = input("Enter Choice (1-6): ")
    
    if choice == "1":
        add_student()
                   
    elif choice == "2":
        update_student()
                   
    elif choice == "3":
        delete_student()
        
    elif choice == "4":
        list_student()
    
    elif choice == "5":
        search_student_skill()
        
    elif choice == "6":
        exist_system()
        break
    else:
        print("Invalid Choice, Please select (1-5)")
    
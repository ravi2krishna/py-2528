# Student Management System

# Menu Based System -> In future once you learn full stack, replace with UI Elements like Buttons 

# System Info - READ ONLY (Tuple)
SYSTEM_INFO = ("Edify Technologies","Student Management System","v1")

# Admin Info - READ ONLY (Tuple)
ADMIN_INFO = ("9090909090","admin@edify.com")

# System Info On Start Up
print("=" * 50)
print(f"Welcome To: {SYSTEM_INFO[0]}")
print(f"Software: {SYSTEM_INFO[1]} - {SYSTEM_INFO[2]}")
print("=" * 50)

# Core Functionality 
# Add Student
# Student Data -> id, name, multiple duplicate scores, multiple unique skills 

# Dictionary To Store Students data 

# id(dict key), name(value), scores(list), skills(set), system info(tuple)

students = {}

# Build Menu Bases System 
while True:
    print("Choose An Option: ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit Application")

    choice = input("Enter Your Option Choice (1-5): ")
    
    if choice == "1":
        print("Adding Student")
        
        student_id = input("Enter ID: ")
        if student_id in students:
            print("Student Already Exists In System")
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
                        print("Invalid Score, Score Should be (0-100)")
                else:
                    print("Invalid Score, Only Digits Allowed")
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input)
            
            # Save above students data to dictionary i.e students = {}  
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            
            print("Student Added")
            print(students)
            
        
    elif choice == "2":
        print("Updating Student")
    elif choice == "3":
        print("Deleting Student")
    elif choice == "4":
        print("Reading Student")
    elif choice == "5":
        print("Exiting Application")
        break
    else:
        print("Invalid Option, Select Only (1-5)")
    

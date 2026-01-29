# OOP Fundamentals 

# class -> Blue Print 
# Student -> Real World Entity 

class Student:
    # has something - Characteristics / Attributes / Variables 
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # does something - Behaviors / Methods 
    def student_info():
        print("Student Studies")
    
    # Statements 
    print("Student Name: "+student_name)
    print("Student Email: "+student_email)
        
# Object Creation 
student_object = Student()
# student_object.student_info() # TypeError: Student.student_info() takes 0 positional arguments but 1 was given

print("=" * 50)

class Student:
    # has something - Characteristics / Attributes / Variables 
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # does something - Behaviors / Methods 
    def student_info(self):
        print("Student Studies")
    
    # Statements 
    print("Student Name: "+student_name)
    print("Student Email: "+student_email)
        
# Object Creation 
student_object = Student()
student_object.student_info()

print("=" * 50)

class Student:
    # has something - Characteristics / Attributes / Variables 
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # does something - Behaviors / Methods 
    def student_info(self):
        print("Student Studies")
        # Statements 
        # print("Student Name: "+student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        # print("Student Email: "+student_email)
        
# Object Creation 
student_object = Student()
student_object.student_info()

print("=" * 50)

class Student:
    # has something - Characteristics / Attributes / Variables 
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # does something - Behaviors / Methods 
    def student_info(self):
        print("Student Studies")
        # Statements 
        print("Student Name: "+self.student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        print("Student Email: "+student_object.student_email)
        
# Object Creation 
student_object = Student()
student_object.student_info()

print("=" * 50)

class Student:
    # has something - Characteristics / Attributes / Variables 
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # does something - Behaviors / Methods 
    def student_info(self):
        print("Student Studies")
        # Statements 
        print("Student Name: "+self.student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        print("Student Email: "+self.student_email)
        
# Object Creation 
student_object = Student()
student_object.student_info()

print("=" * 50)

class Student:
    # has something - Characteristics / Attributes / Variables 
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # does something - Behaviors / Methods 
    def student_info(self):
        print("Student Studies")
        # Statements 
        print("Student Name: "+self.student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        print("Student Email: "+self.student_email)
        
# Object Creation 
student_ravi = Student()
student_ravi.student_info()

student_john = Student()
student_john.student_info()

student_mike = Student()
student_mike.student_info()

print("=" * 50)

class Student:
    # has something - Characteristics / Attributes / Variables 
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor - initialize a newly created object's attributes
    def __init__(self, student_name, student_email):
        self.student_name = student_name
        self.student_email = student_email
    
    # does something - Behaviors / Methods 
    def student_info(self):
        print("Student Studies")
        # Statements 
        print("Student Name: "+self.student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        print("Student Email: "+self.student_email)
        
# Object Creation 
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_info()

student_john = Student("john","john@live.com")
student_john.student_info()

student_mike = Student("mike","mike@yahoo.com")
student_mike.student_info()

print("=" * 50)

class Student:
    # has something - Characteristics / Attributes / Variables 
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor - initialize a newly created object's attributes
    def __init__(self, student_name, student_email):
        # Instance Variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # does something - Behaviors / Methods 
    def student_info(self):
        print("Student Studies")
        # Statements 
        print("Student Name: "+self.student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        print("Student Email: "+self.student_email)
        
# Object Creation 
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_info()

student_john = Student("john","john@live.com")
student_john.student_info()

student_mike = Student("mike","mike@yahoo.com")
student_mike.student_info()

print("=" * 50)

class Student:
    # has something - Characteristics / Attributes / Variables 
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor - initialize a newly created object's attributes
    def __init__(self, student_name, student_email):
        # Instance Variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # does something - Behaviors / Methods 
    # Instance Method
    def student_info(self):
        print("Student Studies")
        # Statements 
        print("Student Name: "+self.student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        print("Student Email: "+self.student_email)
        
# Object Creation 
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_info()

student_john = Student("john","john@live.com")
student_john.student_info()

student_mike = Student("mike","mike@yahoo.com")
student_mike.student_info()

print("=" * 50)

class Student:
    # has something - Characteristics / Attributes / Variables 
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Class Variable - "shared by all the objects" of the class 
    institute_name = "Digital Edify"
    
    # Constructor - initialize a newly created object's attributes
    def __init__(self, student_name, student_email):
        # Instance Variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # does something - Behaviors / Methods 
    # Instance Method
    def student_info(self):
        print("Student Studies")
        print("From Institute: " +Student.institute_name) # this is recommended
        print("From Institute: " +self.institute_name) # this is not recommended
        # Statements 
        print("Student Name: "+self.student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        print("Student Email: "+self.student_email)
        
# Object Creation 
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_info()

student_john = Student("john","john@live.com")
student_john.student_info()

student_mike = Student("mike","mike@yahoo.com")
student_mike.student_info()

print("=" * 50)

class Student:
    # has something - Characteristics / Attributes / Variables 
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Class Variable - "shared by all the objects" of the class 
    institute_name = "Digital Edify"
        
    # Constructor - initialize a newly created object's attributes
    def __init__(self, student_name, student_email):
        # Instance Variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # does something - Behaviors / Methods 
    # Instance Method
    def student_info(self):
        print("Student Studies")
        print("From Institute: " +Student.institute_name) # this is recommended
        print("From Institute: " +self.institute_name) # this is not recommended
        # Statements 
        print("Student Name: "+self.student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        print("Student Email: "+self.student_email)
    
    # Class Method 
    @classmethod
    def change_institute(cls,new_name):
        cls.institute_name = new_name
        # print(self.student_name) # Accessing instance data inside a class method gives error 
        
# Object Creation 
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_info()

student_john = Student("john","john@live.com")
student_john.student_info()

student_mike = Student("mike","mike@yahoo.com")
student_mike.student_info()

# Class Method Accessing
Student.change_institute("Digital Lync")

student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_info()

student_john = Student("john","john@live.com")
student_john.student_info()

student_mike = Student("mike","mike@yahoo.com")
student_mike.student_info()

print("=" * 50)

class Student:
    # has something - Characteristics / Attributes / Variables 
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Class Variable - "shared by all the objects" of the class 
    institute_name = "Digital Edify"
        
    # Constructor - initialize a newly created object's attributes
    def __init__(self, student_name, student_email):
        # Instance Variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # does something - Behaviors / Methods 
    # Instance Method
    def student_info(self):
        print("Student Studies")
        print("From Institute: " +Student.institute_name) # this is recommended
        print("From Institute: " +self.institute_name) # this is not recommended
        # Statements 
        print("Student Name: "+self.student_name) # NameError: name 'student_name' is not defined. Did you mean: 'self.student_name'?
        print("Student Email: "+self.student_email)
    
    # Class Method 
    @classmethod
    def change_institute(cls,new_name):
        cls.institute_name = new_name
        # print(self.student_name) # Accessing instance data inside a class method gives error 
        
    # Static Method     
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email # T and T -> T
    
# Object Creation 
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_info()

student_john = Student("john","john@live.com")
student_john.student_info()

student_mike = Student("mike","mike@yahoo.com")
student_mike.student_info()

# Class Method Accessing
Student.change_institute("Digital Lync")

student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_info()

student_john = Student("john","john@live.com")
student_john.student_info()

student_mike = Student("mike","mike@yahoo.com")
student_mike.student_info()

# Static Method Accessing
print(Student.validate_email("ravi"))
print(Student.validate_email("ravi@gmailcom"))
print(Student.validate_email("ravi@gmail.com"))

print("=" * 50)


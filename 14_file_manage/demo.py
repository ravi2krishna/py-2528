# Working With Files & Folders
# Using Persistent Storage 

# Syntax - 1
file = open("14_file_manage/file.txt","r")
print(file)
print(file.closed)
file.close()
print(file.closed)

# Syntax - 2
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data)
print(file_data.closed)

# Read Mode
# Reading Data From File - Whole file
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.read())

# Reading Data From File - Character wise 
with open("14_file_manage/file.txt","r") as file_data:
    for char in file_data.read():
        print(char)
        
# Reading Data From File - Word wise 
with open("14_file_manage/file.txt","r") as file_data:
    for word in file_data.read().split():
        print(word)
        
# Reading Data From File - Line wise 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readline())
    
# Reading Data From File - Line wise 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readlines())

# Reading Data From File - Line wise 
with open("14_file_manage/file.txt","r") as file_data:
    for line in file_data.readlines():
        print(line)
        
# Reading Data From File - Line wise 
with open("14_file_manage/file.txt","r") as file_data:
    for line in file_data.readlines():
        print(line.strip())
        
# Write Mode 

# Create file 
with open("14_file_manage/write.txt","w") as file_data:
    print(file_data)
    
# Write Data To File Using "w" mode
with open("14_file_manage/write.txt","w") as file_data:
    file_data.write("Hi there")

# Write Data To File Using "w" mode multiple lines
with open("14_file_manage/write.txt","w") as file_data:
    file_data.writelines(['Hello there\n', 'how are you'])

# Write Data To File Using "w" mode - Overwrites Data 
with open("14_file_manage/write.txt","w") as file_data:
    file_data.writelines(['are you coming to class today\n', 'please confirm'])
  
 
# Append Mode    
# append Data To File Using "a" mode multiple lines
with open("14_file_manage/new.txt","a") as file_data:
    file_data.writelines(['Hello there\n', 'how are you\n'])

# append Data To File Using "a" mode - Appends Data 
with open("14_file_manage/new.txt","a") as file_data:
    file_data.writelines(['are you coming to class today\n', 'please confirm'])
    
# Create Folder 
import os 
dir_name = "14_file_manage/students_data"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

# Create File In Above Dir
with open("14_file_manage/students_data/student.txt","w") as file_data:
    print(file_data)

# Delete File 
os.remove("14_file_manage/new.txt")

# Delete Empty Folder 
dir_name = "14_file_manage/hello"
# os.rmdir(dir_name)

dir_name = "14_file_manage/students_data"
# os.rmdir(dir_name) # OSError: [Errno 66] Directory not empty: '14_file_manage/students_data'

# Delete Non-Empty Folder 
import shutil
dir_name = "14_file_manage/students_data"
shutil.rmtree(dir_name)
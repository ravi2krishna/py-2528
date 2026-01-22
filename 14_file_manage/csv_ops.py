# Working With CSV Files

import csv

# Read CSV Data 
with open("14_file_manage/students.csv","r") as file_data:
    # print(file_data.read())
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)

print("=" * 50)

# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from Hyderabad  
filter_by_city = "Hyderabad"   
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row[3])
        if row[3] == filter_by_city:
            print(row)

print("=" * 50)
            
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from tcs   
filter_by_email = "@tcs.com"   
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row[3])
        if row[1].endswith(filter_by_email):
            print(row)

print("=" * 50)

# Because of new requirements, data format changed            
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from tcs   
filter_by_email = "@tcs.com"   
with open("14_file_manage/new_students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row[3])
        if row[3].endswith(filter_by_email):
            print(row)
            
print("=" * 50)

# DictReader
# Assume We Have 10K -> 100k Students Records In CSV File 
# Customer Requirement: Fetch me all the students from tcs   
filter_by_email = "@tcs.com"   
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row)
        if row['email'].endswith(filter_by_email):
            print(row)
 
print("=" * 50)
            
filter_by_email = "@tcs.com"   
with open("14_file_manage/new_students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row)
        if row['email'].endswith(filter_by_email):
            print(row)

# Write CSV Data - Overwrite 
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    row = ["name","email","mobile","address"]
    csv_writer.writerow(row)
    csv_writer.writerow(['Ravi', 'ravi525@tcs.com', '9234792360', 'Coimbatore'])
    csv_writer.writerow(['Kishore', 'kishore349@tcs.com', '9900803042', 'Hyderabad'])
    csv_writer.writerow(['Balu', 'balu57@tcs.com', '9599915040', 'Coimbatore'])
    
    rows = [['Kiran', 'kiran825@tcs.com', '9117722204', 'Chennai'],
            ['Anil', 'anil570@tcs.com', '9349511781', 'Bangalore'],
            ['Vijay', 'vijay115@tcs.com', '9333459882', 'Delhi']]
    csv_writer.writerows(rows)


# Write CSV Data - Append 
with open("14_file_manage/emp.csv","a") as file_data:
    csv_writer = csv.writer(file_data)
    row = ["name","email","mobile","address"]
    csv_writer.writerow(row)
    csv_writer.writerow(['Ravi', 'ravi525@tcs.com', '9234792360', 'Coimbatore'])
    csv_writer.writerow(['Kishore', 'kishore349@tcs.com', '9900803042', 'Hyderabad'])
    csv_writer.writerow(['Balu', 'balu57@tcs.com', '9599915040', 'Coimbatore'])
    
    rows = [['Kiran', 'kiran825@tcs.com', '9117722204', 'Chennai'],
            ['Anil', 'anil570@tcs.com', '9349511781', 'Bangalore'],
            ['Vijay', 'vijay115@tcs.com', '9333459882', 'Delhi']]
    csv_writer.writerows(rows)
    
# Write CSV Data - Overwrite 
    fieldnames = ["name","email","mobile","address"]
    with open("14_file_manage/person.csv","w") as file_data:
        # csv_writer = csv.DictWriter(file_data) # TypeError: DictWriter.__init__() missing 1 required positional argument: 'fieldnames'
        csv_writer = csv.DictWriter(file_data,fieldnames) 
        csv_writer.writeheader()
        csv_writer.writerow({'name': 'Ravi', 'email': 'ravi457@tcs.com', 'mobile': '9453895721', 'address': 'Jaipur'})
        csv_writer.writerows([{'name': 'Manoj', 'email': 'manoj354@tcs.com', 'mobile': '9381899128', 'address': 'Chennai'},
                              {'name': 'Ramu', 'email': 'ramu661@tcs.com', 'mobile': '9833214959', 'address': 'Bangalore'},
                              {'name': 'Deepak', 'email': 'deepak641@tcs.com', 'mobile': '9369382025', 'address': 'Chennai'}])
        

# Write CSV Data - Append 
    fieldnames = ["name","email","mobile","address"]
    with open("14_file_manage/person.csv","a") as file_data:
        # csv_writer = csv.DictWriter(file_data) # TypeError: DictWriter.__init__() missing 1 required positional argument: 'fieldnames'
        csv_writer = csv.DictWriter(file_data,fieldnames) 
        csv_writer.writeheader()
        csv_writer.writerow({'name': 'Ravi', 'email': 'ravi457@tcs.com', 'mobile': '9453895721', 'address': 'Jaipur'})
        csv_writer.writerows([{'name': 'Manoj', 'email': 'manoj354@tcs.com', 'mobile': '9381899128', 'address': 'Chennai'},
                              {'name': 'Ramu', 'email': 'ramu661@tcs.com', 'mobile': '9833214959', 'address': 'Bangalore'},
                              {'name': 'Deepak', 'email': 'deepak641@tcs.com', 'mobile': '9369382025', 'address': 'Chennai'}])
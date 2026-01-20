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


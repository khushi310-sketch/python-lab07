import csv

file = open("students.csv", "r")

reader = csv.DictReader(file)

search_name = input("Enter student name: ")

found = False

for row in reader:
    if row["Name"].lower() == search_name.lower():
        print("Name:", row["Name"])
        print("Marks:", row["Marks"])
        found = True

if found == False:
    print("Student not found")

file.close()
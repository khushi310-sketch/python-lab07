import csv

file = open("students.csv", "r")

reader = csv.DictReader(file)

for row in reader:
    print("Name:", row["Name"])
    print("Marks:", row["Marks"])

file.close()
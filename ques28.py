import csv

file = open("students.csv", "r")

reader = csv.DictReader(file)

highest_marks = -1
topper = ""

for row in reader:
    marks = int(row["Marks"])

    if marks > highest_marks:
        highest_marks = marks
        topper = row["Name"]

print("Highest Marks:", highest_marks)
print("Topper:", topper)

file.close()
import csv

file = open("students.csv", "a", newline="")

writer = csv.writer(file)

writer.writerow(["Priya", 95])

file.close()

print("New record added successfully")
import csv

file = open("students.csv", "r")

reader = csv.reader(file)

rows = list(reader)

print("Number of rows:", len(rows) - 1)
print("Number of columns:", len(rows[0]))

file.close()
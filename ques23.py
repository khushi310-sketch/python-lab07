import csv

file = open("students.csv", "r")

reader = csv.reader(file)
next(reader)

total = 0
count = 0

for row in reader:
    total += int(row[1])
    count += 1

average = total / count

print("Average Marks:", average)

file.close()
import csv

source = open("students.csv", "r")
destination = open("copy.csv", "w", newline="")

reader = csv.reader(source)
writer = csv.writer(destination)

for row in reader:
    writer.writerow(row)

source.close()
destination.close()

print("CSV data copied successfully")
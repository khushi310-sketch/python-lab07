import csv

file1 = open("students1.csv", "r")
file2 = open("students2.csv", "r")
file3 = open("combined.csv", "w", newline="")

reader1 = csv.reader(file1)
reader2 = csv.reader(file2)
writer = csv.writer(file3)

header = next(reader1)
next(reader2)

writer.writerow(header)

for row in reader1:
    writer.writerow(row)

for row in reader2:
    writer.writerow(row)

file1.close()
file2.close()
file3.close()

print("CSV files combined successfully")
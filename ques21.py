import csv

file = open("students.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow(["Name", "Marks"])
writer.writerow(["Aman", 85])
writer.writerow(["Riya", 90])
writer.writerow(["Rahul", 78])

file.close()

print("CSV file created successfully")
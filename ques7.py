file = open("multiple.txt", "w")

n = int(input("How many lines do you want to enter? "))

for i in range(n):
    line = input("Enter line: ")
    file.write(line + "\n")

file.close()

print("All lines saved successfully.")
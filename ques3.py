file = open("sample.txt", "r")

print("Reading file line by line:")

for line in file:
    print(line, end="")

file.close()
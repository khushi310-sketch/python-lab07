file = open("sample.txt", "r")

line_number = 1

for line in file:
    if line_number % 2 == 0:
        print(line, end="")

    line_number += 1

file.close()
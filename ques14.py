file = open("sample.txt", "r")

longest_line = ""

for line in file:
    if len(line) > len(longest_line):
        longest_line = line

print("Longest line:", longest_line.strip())

file.close()
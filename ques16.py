file = open("sample.txt", "r")

lines = file.readlines()

if len(lines) > 0:
    print("First line:", lines[0].strip())
    print("Last line:", lines[-1].strip())
else:
    print("File is empty")

file.close()
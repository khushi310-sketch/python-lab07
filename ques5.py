file = open("sample.txt", "r")

content = file.read()

lines = content.splitlines()

line_count = len(lines)
character_count = len(content)

print("Total lines:", line_count)
print("Total characters:", character_count)

file.close()
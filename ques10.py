file = open("sample.txt", "r")

content = file.read()

uppercase_content = content.upper()

print("Uppercase Content:")
print(uppercase_content)

file.close()
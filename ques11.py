file = open("sample.txt", "r")

content = file.read()
word = input("Enter word to search: ")

if word.lower() in content.lower().split():
    print("Word found in file")
else:
    print("Word not found")

file.close()
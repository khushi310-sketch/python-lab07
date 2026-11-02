file = open("sample.txt", "r")

content = file.read()
words = content.lower().split()

word = input("Enter word: ").lower()

count = 0

for w in words:
    if w == word:
        count += 1

print("Word occurrence:", count)

file.close()
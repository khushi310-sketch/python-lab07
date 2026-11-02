file = open("sample.txt", "r")

words = file.read().split()
file.close()

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

file = open("unique.txt", "w")

for word in unique_words:
    file.write(word + "\n")

file.close()

print("Unique words saved successfully")
file = open("sample.txt", "r")

words = file.read().split()
file.close()

words.sort(key=str.lower)

file = open("sorted.txt", "w")

for word in words:
    file.write(word + "\n")

file.close()

print("Words sorted successfully")
file = open("sample.txt", "a")

new_text = input("Enter new content: ")

file.write("\n" + new_text)

file.close()

print("Content appended successfully.")
file = open("numbers.txt", "r")

numbers = list(map(int, file.read().split()))

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

file.close()
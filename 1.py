numbers = [8, 3, 12, 4, 7, 2]

for i in range(len(numbers)):
    if numbers[i] <4:
        numbers[i] = 0

numbers.sort(reverse=True)

print(numbers)
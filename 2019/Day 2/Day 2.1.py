input_data = open("input.txt").read().split(",")
numbers = []
for data in input_data:
    numbers.append(int(data))

numbers[1] = 12
numbers[2] = 2
index = 0
while index < len(numbers):
    up_code = numbers[index]
    if up_code == 1:
        numbers[numbers[index + 3]] = numbers[numbers[index + 1]] + numbers[numbers[index + 2]]
    elif up_code == 2:
        numbers[numbers[index + 3]] = numbers[numbers[index + 1]] * numbers[numbers[index + 2]]
    elif up_code == 99:
        break
    index += 4

print(numbers)

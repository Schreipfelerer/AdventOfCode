input_data = open("input.txt").read().split(",")
original_numbers = []
for data in input_data:
    original_numbers.append(int(data))

for noun in range(0, 100):
    for verb in range(0, 100):
        numbers = original_numbers[:]
        numbers[1] = noun
        numbers[2] = verb
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

        if numbers[0] == 19690720:
            print(str(noun * 100 + verb))
            exit()

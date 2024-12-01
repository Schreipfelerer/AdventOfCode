turn = 1
spoken = {}
starting_numbers = [int(string) for string in open("input.txt").readline().split(",")]

for number in starting_numbers[:-1]:
    spoken[number] = turn
    turn += 1

num = starting_numbers[-1]
while turn < 2020:
    try:
        last_spoken = spoken[num]
        spoken[num] = turn
        num = turn - last_spoken
    except KeyError:
        spoken[num] = turn
        num = 0
    turn += 1

print(num)

import functools

def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        data.append(line.rstrip("\n").split(" "))
    return data


def solve(data):  # solves the question
    winnings = 0
    data.sort(key=functools.cmp_to_key(compare))
    for i, hand in enumerate(data):
        winnings += (i+1)*int(hand[1])
    return winnings


def compare(item1, item2):
    hand1 = item1
    hand2 = item2
    hand1_dc = len(set(hand1[0]))
    hand2_dc = len(set(hand2[0]))

    if hand1_dc > hand2_dc:
        return -1
    if hand1_dc < hand2_dc:
        return 1

    hand1_mfo = 0
    for card in set(hand1[0]):
        count = hand1[0].count(card)
        if hand1_mfo < count:
            hand1_mfo = count
    hand2_mfo = 0
    for card in set(hand2[0]):
        count = hand2[0].count(card)
        if hand2_mfo < count:
            hand2_mfo = count

    if hand1_mfo > hand2_mfo:
        return 1
    if hand1_mfo < hand2_mfo:
        return -1

    for i in range(5):
        index1 = "23456789TJQKA".index(hand1[0][i])
        index2 = "23456789TJQKA".index(hand2[0][i])
        if index1 > index2:
            return 1
        if index1 < index2:
            return -1
    return 0


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()

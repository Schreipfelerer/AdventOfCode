from typing import List


def readInput(use_example=False) -> List[str]:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    nums = []
    for n in lines[0].rstrip("\n").split(","):
        nums.append(int(n))
    lines = lines[2:]

    bingo_boards = []
    board = []
    for line in lines:
        if not line.rstrip("\n"):
            bingo_boards.append(board)
            board = []
        else:
            kek = []
            for element in line.lstrip(" ").rstrip("\n").replace("  ", " ").split(" "):
                kek.append(int(element))
            board.append(kek)
    bingo_boards.append(board)

    return nums, bingo_boards


def solve(data):  # solves the question
    nums, bingo_boards = data
    num_index = 0
    num_drawn = None
    has_won = False
    board_won = None

    while not has_won:
        num_drawn = nums[num_index]
        for board in bingo_boards:
            for line in board:
                for element in line:
                    if element == num_drawn:
                        line[line.index(element)] = -1

        for board in bingo_boards:
            for line in board:
                if sum(line) == -5:
                    has_won = True
                    board_won = board

        for board in bingo_boards:
            for i in range(5):
                sum_vertical = 0
                for line in board:
                    sum_vertical += line[i]
                if sum_vertical == -5:
                    has_won = True
                    board_won = board

        num_index += 1

    sum_unmarked = 0
    for line in board_won:
        for element in line:
            if element != -1:
                sum_unmarked += element

    return sum_unmarked * num_drawn


def main():
    lines = readInput(False)
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()

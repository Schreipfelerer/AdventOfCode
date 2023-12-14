def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        data.append((line[0], int(line.split(" ")[1])))
    return data


def solve(data):  # solves the question
    vis_pos = set()
    vis_pos.add((0, 0))
    tail = [0, 0]
    head = [0, 0]
    for move in data:
        for _ in range(move[1]):
            if move[0] == "R":
                head[0] += 1
            elif move[0] == "L":
                head[0] -= 1
            elif move[0] == "U":
                head[1] += 1
            elif move[0] == "D":
                head[1] -= 1

            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                if tail[0] == head[0]:
                    tail[1] += 1 if head[1] > tail[1] else -1
                elif tail[1] == head[1]:
                    tail[0] += 1 if head[0] > tail[0] else -1
                else:
                    tail[1] += 1 if head[1] > tail[1] else -1
                    tail[0] += 1 if head[0] > tail[0] else -1
                vis_pos.add((tail[0], tail[1]))
    return len(vis_pos)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()

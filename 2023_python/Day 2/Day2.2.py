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
        line = line.lstrip("Game ").rstrip("\n")
        game_id = int(line.split(": ")[0])
        revealed = line.split(": ")[1].split("; ")
        set_dics = []
        for sets in revealed:
            set_dic = dict()
            for cube in sets.split(", "):
                set_dic[cube.split(" ")[1]] = int(cube.split(" ")[0])
            set_dics.append(set_dic)
        data.append((game_id, set_dics))
    return data


def solve(data):  # solves the question
    id_sum = 0
    for game in data:
        reds = 0
        greens = 0
        blues = 0
        for game_set in game[1]:
            if "red" in game_set and game_set["red"] > reds:
                reds = game_set["red"]
            if "green" in game_set and game_set["green"] > greens:
                greens = game_set["green"]
            if "blue" in game_set and game_set["blue"] > blues:
                blues = game_set["blue"]

        id_sum += reds * greens * blues
    return id_sum


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()

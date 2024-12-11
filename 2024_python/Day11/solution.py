def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    data = list(map(int, lines[0].split(" ")))
    data_dict = {}
    for d in data:
        data_dict[d] = 1

    return data_dict

def solve_part1(data):  # solves the question
    return blink(data, 25)


def solve_part2(data):
    return blink(data, 75)


def blink(data_dict, i):  # solves the question
    for _ in range(i):
        new_data = {}
        for d in data_dict:
            str_d = str(d)
            if d == 0:
                dic_add(new_data, 1, data_dict[d])
            elif len(str_d) % 2 == 0:
                dic_add(new_data, int(str_d[: len(str_d) // 2]), data_dict[d])
                dic_add(new_data, int(str_d[len(str_d) // 2 :]), data_dict[d])
            else:
                dic_add(new_data, d * 2024, data_dict[d])
        data_dict = new_data
    return sum(data_dict.values())


def dic_add(dic, key, to_add):
    if key in dic:
        dic[key] += to_add
    else:
        dic[key] = to_add


def main():
    lines = read_input()
    data = parse_input(lines)
    print(f"Part 1: {solve_part1(data)}")
    print()
    print(f"Part 2: {solve_part2(data)}")


if __name__ == "__main__":
    main()

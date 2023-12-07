import ast

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
        data.append(line.rstrip("\n"))
    return data


def solve(data):  # solves the question
    largest_mag = 0
    for num1 in data:
        for num2 in data:
            if num1 != num2:
                number = "["+num1+","+num2+"]"
                fully_reduced = False

                while not fully_reduced:
                    old_num = number
                    number = explode(number)
                    if old_num == number:
                        number = split(number)
                    if old_num == number:
                        fully_reduced = True
                maginitute = mag(ast.literal_eval(number))
                if maginitute > largest_mag:
                    largest_mag = maginitute
    return largest_mag


def mag(e):
    if type(e) == int:
        return e
    return mag(e[0])*3 + mag(e[1])*2


def explode(number):
    layer = 0
    leftmost_index = -1
    rightmost_index = -1
    break_index = -1
    break_stop_index = -1
    doneWithExplodingPair = False
    for i, s in enumerate(number):
        if s == "[":
            layer += 1
            if layer == 5 and break_index == -1:
                break_index = i
        if s == "]":
            layer -= 1
            if layer == 4 and break_index != -1 and break_stop_index == -1:
                doneWithExplodingPair = True
                break_stop_index = i
        if s in "0123456789":
            if break_index == -1:
                leftmost_index = i
            elif doneWithExplodingPair and rightmost_index == -1:
                rightmost_index = i

    leftreplace = -1
    rightreplace = -1
    offset = 0
    if break_index != -1:
        leftnum = int(number[break_index+1:break_stop_index].split(",")[0])
        rightnum = int(number[break_index+1:break_stop_index].split(",")[1])
        left_is_two_digit = False
        right_is_two_digit = False
        if leftmost_index != -1:
            leftreplace = leftnum + int(number[leftmost_index])
            if number[leftmost_index-1] in "0123456789":
                leftreplace = leftnum + int(number[leftmost_index-1:leftmost_index+1])
                left_is_two_digit = True
        if rightmost_index != -1:
            rightreplace = rightnum + int(number[rightmost_index])
            if number[rightmost_index+1] in "0123456789":
                rightreplace = rightnum + int(number[rightmost_index:rightmost_index+2])
                right_is_two_digit = True

        if leftreplace != -1:
            number = number[:leftmost_index] + str(leftreplace) + number[leftmost_index + 1:]
            if leftreplace >= 10:
                offset += 1
            if left_is_two_digit:
                offset -= 1
                number = number[:leftmost_index-1] + number[leftmost_index:]
        if rightreplace != -1:
            if right_is_two_digit:
                number = number[:rightmost_index+1] + number[rightmost_index+2:]
            number = number[:rightmost_index + offset] + str(rightreplace) + number[rightmost_index + offset + 1:]
        number = number[:break_index+offset]+"0"+number[break_stop_index+offset+1:]

    return number


def split(number):
    break_index = -1
    last_num = -1
    for i, s in enumerate(number):
        if s in "0123456789" and break_index == -1:
            if last_num == -1:
                last_num = s
            else:
                break_index = i
        else:
            last_num = -1

    if break_index != -1:
        oldnum = int(number[break_index-1]+number[break_index])
        if oldnum % 2 == 0:
            newnum = f"[{int(oldnum / 2)},{int(oldnum / 2)}]"
        else:
            newnum = f"[{int(oldnum / 2)},{int(oldnum / 2)+1}]"

        number = number[:break_index-1]+newnum+number[break_index+1:]

    return number


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()

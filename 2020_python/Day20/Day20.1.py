def border_is_equal(b1, b2):
    return b1 == b2 or b1 == b2[::-1]


class Tile:
    def __init__(self, tile_str):
        self.number = int(tile_str.split("\n")[0].split(" ")[1].rstrip(":"))
        self.borders = [tile_str.split("\n")[1], tile_str.split("\n")[-1]]
        left_b = ""
        right_b = ""
        for i in range(1, len(tile_str.split("\n"))):
            left_b += tile_str.split("\n")[i][0]
            right_b += tile_str.split("\n")[i][-1]
        self.borders.append(left_b)
        self.borders.append(right_b)

    def compareToRest(self, other_tiles):
        matching_boarders = 0
        for border in self.borders:
            is_matching = False
            for other_tile in other_tiles:
                if self.number != other_tile.number:
                    for tile_boarder in other_tile.borders:
                        if border_is_equal(border, tile_boarder):
                            is_matching = True
            if is_matching:
                matching_boarders += 1

        if matching_boarders == 2:
            print(self.number)
            return self.number
        elif matching_boarders == 3 or matching_boarders == 4:
            return 1
        else:
            print("weniger als 2..." + str(self.number))
            return 1


with open("input.txt") as file:
    tile_strings = file.read().split("\n\n")
tiles = []
for tile_string in tile_strings:
    tiles.append(Tile(tile_string))

num = 1
for tile in tiles:
    num *= tile.compareToRest(tiles)

print(num)

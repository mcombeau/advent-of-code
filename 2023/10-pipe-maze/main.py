import argparse

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Map = list[str]


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


#       PART ONE


class Position:
    def __init__(self, y, x):
        self.y: int = y
        self.x: int = x

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented
        return self.y == other.y and self.x == other.x


def find_animal_pos(map: Map) -> Position:
    pos: Position = Position(-1, -1)

    for y, row in enumerate(map):
        for x, col in enumerate(row):
            if map[y][x] == "S":
                pos = Position(y, x)

    return pos


def find_starting_pos(map: Map, pos: Position) -> Position:
    north: Position = Position(pos.y - 1, pos.x)
    east: Position = Position(pos.y, pos.x + 1)
    south: Position = Position(pos.y + 1, pos.x)
    west: Position = Position(pos.y, pos.x - 1)

    if is_loop_tile(map, north, "|7F"):
        return north
    if is_loop_tile(map, east, "-J7"):
        return east
    if is_loop_tile(map, south, "|LJ"):
        return south
    if is_loop_tile(map, west, "-LF"):
        return west

    return Position(-1, -1)


def is_loop_tile(map: Map, pos: Position, valid_tiles: str) -> bool:
    if pos.x < 0 or pos.x > len(map[0]) or pos.y < 0 or pos.y > len(map):
        return False

    if map[pos.y][pos.x] in valid_tiles:
        return True

    return False


def get_next_pos(map: Map, pos: Position, visited_tiles: list[Position]) -> Position:
    north: Position = Position(pos.y - 1, pos.x)
    east: Position = Position(pos.y, pos.x + 1)
    south: Position = Position(pos.y + 1, pos.x)
    west: Position = Position(pos.y, pos.x - 1)

    match map[pos.y][pos.x]:
        case "L":
            return east if north in visited_tiles else north
        case "J":
            return west if north in visited_tiles else north
        case "F":
            return south if east in visited_tiles else east
        case "7":
            return south if west in visited_tiles else west
        case "-":
            return east if west in visited_tiles else west
        case "|":
            return south if north in visited_tiles else north

    return Position(-1, -1)


def calculate_result_part_1(map: Map) -> int:
    steps: int = 1
    starting_pos: Position = find_animal_pos(map)
    visited_tiles: list[Position] = [starting_pos]
    pos: Position = find_starting_pos(map, visited_tiles[0])

    print(f"Current pos: map[{pos.y}][{pos.x}]: {map[pos.y][pos.x]}", end="\r")

    while map[pos.y][pos.x] != "S":
        visited_tiles.append(pos)
        pos = get_next_pos(map, pos, visited_tiles)

        print(end="\x1b[2K")
        print(f"Current pos: map[{pos.y}][{pos.x}]: {map[pos.y][pos.x]}", end="\r")

        if steps == 1:
            visited_tiles.pop(0)
        steps += 1

    print()
    return int(steps / 2)


#       PART TWO


def calculate_result_part_2(map: Map) -> int:
    return 0


#       MAIN


def main() -> None:
    args: Args = parse_args()
    with open(args.filename) as file:
        lines: list[str] = file.readlines()

    result: int = calculate_result_part_1(lines)
    print(f"Part 1 Result: {result}")

    result: int = calculate_result_part_2(lines)
    print(f"Part 2 Result: {result}")
    exit(0)


if __name__ == "__main__":
    main()

import argparse
from enum import IntEnum

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Map = list[str]


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


class Dir(IntEnum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3
    ERROR = -1


class Direction:
    def __init__(self, dir, pos, valid_tiles):
        self.dir: Dir = dir
        self.pos: tuple[int, int] = pos
        self.valid_tiles: str = valid_tiles


#       PART ONE


def get_future_direction(current_dir: Dir, tile: str) -> Dir:
    match current_dir:
        case Dir.EAST:
            if tile == "-":
                return Dir.EAST
            elif tile == "7":
                return Dir.SOUTH
            elif tile == "J":
                return Dir.NORTH
        case Dir.SOUTH:
            if tile == "|":
                return Dir.SOUTH
            elif tile == "L":
                return Dir.EAST
            elif tile == "J":
                return Dir.WEST
        case Dir.WEST:
            if tile == "-":
                return Dir.WEST
            elif tile == "F":
                return Dir.SOUTH
            elif tile == "L":
                return Dir.NORTH
        case Dir.NORTH:
            if tile == "|":
                return Dir.NORTH
            elif tile == "F":
                return Dir.EAST
            elif tile == "7":
                return Dir.WEST
    return Dir.ERROR


def get_starting_dirs(dirs: list[Direction], map: Map, ay: int, ax: int) -> list[Dir]:
    starting_dirs: list[Dir] = []

    for i in range(len(dirs)):
        by = ay + dirs[i].pos[0]
        bx = ax + dirs[i].pos[1]
        if (
            by >= 0
            and by <= len(map)
            and bx >= 0
            and bx <= len(map[0])
            and map[by][bx] in dirs[i].valid_tiles
        ):
            starting_dirs.append(dirs[i].dir)

    return starting_dirs


def get_starting_coordinates(map: Map) -> tuple[int, int]:
    ay, ax = -1, -1

    for y in range(len(map)):
        if "S" in map[y]:
            ay = y
            ax = map[y].find("S")

    return ay, ax


def init_directions() -> list[Direction]:
    dirs: list[Direction] = []

    dirs.append(Direction(Dir.EAST, (0, 1), "-7J"))
    dirs.append(Direction(Dir.SOUTH, (1, 0), "|LJ"))
    dirs.append(Direction(Dir.WEST, (0, -1), "-FL"))
    dirs.append(Direction(Dir.NORTH, (-1, 0), "|F7"))

    return dirs


def calculate_result_part_1(map: Map) -> int:
    dirs: list[Direction] = init_directions()

    ay: int
    ax: int
    ay, ax = get_starting_coordinates(map)

    current_dir: Dir = get_starting_dirs(dirs, map, ay, ax)[0]

    y: int = ay + dirs[current_dir].pos[0]
    x: int = ax + dirs[current_dir].pos[1]
    steps: int = 1

    while (y, x) != (ay, ax):
        current_dir: Dir = get_future_direction(current_dir, map[y][x])
        y = y + dirs[current_dir].pos[0]
        x = x + dirs[current_dir].pos[1]
        steps += 1

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

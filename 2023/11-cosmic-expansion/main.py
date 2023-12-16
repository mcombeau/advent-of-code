import argparse
import copy

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Universe = list[list[int]]

SPACE: int = 0
GALAXY: int = 1


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


def get_universe(lines: list[str]) -> Universe:
    universe: Universe = [[SPACE] * len(lines[0]) for _ in range(len(lines))]

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                universe[y][x] = GALAXY

    return universe


def expand_universe_rows(universe) -> Universe:
    expanded_universe: Universe = []

    for y in range(len(universe)):
        if 1 in universe[y]:
            expanded_universe.append(universe[y])
        else:
            expanded_universe.append(universe[y])
            expanded_universe.append(universe[y])

    return expanded_universe


def expand_universe_cols(universe) -> Universe:
    expanded_universe: Universe = copy.deepcopy(universe)
    cols_to_expand: list[int] = []

    for x in range(len(universe[0]) - 1):
        found_galaxy: bool = False
        for y in range(len(universe)):
            if universe[y][x] == GALAXY:
                found_galaxy = True
                continue
        if found_galaxy == False:
            cols_to_expand.append(x)

    for i, col in enumerate(cols_to_expand):
        for y in range(len(expanded_universe)):
            expanded_universe[y].insert(col + i, 0)

    return expanded_universe


def get_expanded_universe(lines: list[str]) -> Universe:
    universe: Universe = get_universe(lines)
    universe = expand_universe_cols(universe)
    universe = expand_universe_rows(universe)

    return universe


def get_distances_from_galaxies(universe: Universe, pos: tuple[int, int]) -> int:
    distances: list[int] = []

    for y in range(len(universe)):
        for x in range(len(universe[0])):
            if y == pos[0] and x == pos[1]:
                continue
            if universe[y][x] == GALAXY:
                distances.append(abs(pos[0] - y) + abs(pos[1] - x))

    return sum(distances)


#       PART ONE


def calculate_result_part_1(lines: list[str]) -> int:
    universe: Universe = get_expanded_universe(lines)
    distances: list[int] = []

    for y in range(len(universe)):
        for x in range(len(universe[0])):
            if universe[y][x] == GALAXY:
                distances.append(get_distances_from_galaxies(universe, (y, x)))
                universe[y][x] = 0

    return sum(distances)


#       PART TWO


def calculate_result_part_2(lines: list[str]) -> int:
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

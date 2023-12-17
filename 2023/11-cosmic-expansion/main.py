import argparse

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Universe = list[list[int]]
Coord = tuple[int, int]
EmptySpace = list[list[int]]

SPACE: int = 0
GALAXY: int = 1


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


def get_universe(lines: list[str]) -> Universe:
    return [
        [GALAXY if lines[y][x] == "#" else SPACE for x in range(len(lines[0]))]
        for y in range(len(lines))
    ]


def get_empty_space(universe: Universe) -> EmptySpace:
    empty_space: EmptySpace = []

    empty_space.append([y for y in range(len(universe)) if GALAXY not in universe[y]])
    empty_space.append(
        [
            x
            for x in range(len(universe[0]) - 1)
            if all(row[x] != GALAXY for row in universe)
        ]
    )

    return empty_space


def get_empty_space_between(empty_space: list[int], coords: list[int]) -> int:
    coords.sort()
    return sum(1 for space in empty_space if space in range(coords[0], coords[1]))


def get_distance_between(
    space: EmptySpace,
    expansion: int,
    g1: Coord,
    g2: Coord,
) -> int:
    diff = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    diff += get_empty_space_between(space[0], [g1[0], g2[0]]) * (expansion - 1)
    diff += get_empty_space_between(space[1], [g1[1], g2[1]]) * (expansion - 1)

    return diff


def get_distances_from_other_galaxies(
    universe: Universe,
    space: EmptySpace,
    expansion: int,
    pos: Coord,
) -> int:
    return sum(
        get_distance_between(space, expansion, pos, (y, x))
        for y in range(len(universe))
        for x in range(len(universe[0]))
        if (y, x) != pos and universe[y][x] == GALAXY
    )


def get_all_distances(
    universe: Universe, space: EmptySpace, expansion_rate: int
) -> int:
    distances: list[int] = []

    for y in range(len(universe)):
        for x in range(len(universe[0])):
            if universe[y][x] == GALAXY:
                distances.append(
                    get_distances_from_other_galaxies(
                        universe, space, expansion_rate, (y, x)
                    )
                )
                universe[y][x] = 0

    return sum(distances)


#       PART ONE


def calculate_result_part_1(lines: list[str]) -> int:
    universe: Universe = get_universe(lines)
    empty_space: EmptySpace = get_empty_space(universe)

    return get_all_distances(universe, empty_space, expansion_rate=2)


#       PART TWO


def calculate_result_part_2(lines: list[str]) -> int:
    universe: Universe = get_universe(lines)
    empty_space: EmptySpace = get_empty_space(universe)

    return get_all_distances(universe, empty_space, expansion_rate=1000000)


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

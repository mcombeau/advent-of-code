import argparse

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Grid = list[str]


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


def roll_rocks_left(grid: Grid) -> Grid:
    tilted_grid: Grid = []
    for row in grid:
        rolled_rocks: list[str] = []

        for group in row.split("#"):
            rolled: str = "".join(sorted(list(group), reverse=True))
            rolled_rocks.append(rolled)

        rolled_row = "#".join(rolled_rocks)
        tilted_grid.append(rolled_row)

    return tilted_grid


def calculate_load(grid: Grid) -> int:
    result: int = 0

    for i, row in enumerate(grid):
        rock_count = row.count("O")
        result += rock_count * (len(grid) - i)

    return result


#       PART ONE


def calculate_result_part_1(lines: list[str]) -> int:
    grid: Grid = [line.strip() for line in lines]
    rotated_grid: Grid = list(map("".join, zip(*grid)))
    tilted_grid: Grid = roll_rocks_left(rotated_grid)
    grid = list(map("".join, zip(*tilted_grid)))

    return calculate_load(grid)


#       PART TWO


def cycle(grid: tuple[str, ...]) -> tuple[str, ...]:
    for _ in range(4):
        rotated_grid: Grid = list(map("".join, zip(*grid)))
        tilted_grid: Grid = roll_rocks_left(rotated_grid)
        grid = tuple(row[::-1] for row in tilted_grid)
    return grid


def calculate_result_part_2(lines: list[str]) -> int:
    grid: tuple[str, ...] = tuple(line.strip() for line in lines)
    seen_grid_hashes: set = {grid}
    seen_grids: list[tuple[str, ...]] = [grid]
    i: int = 0

    while True:
        i += 1
        grid = cycle(grid)
        if grid in seen_grid_hashes:
            break
        seen_grids.append(grid)
        seen_grid_hashes.add(grid)

    offset = seen_grids.index(grid)

    grid: tuple[str, ...] = seen_grids[(1000000000 - offset) % (i - offset) + offset]

    return calculate_load(list(grid))


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

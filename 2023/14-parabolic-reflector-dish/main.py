import argparse

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Grid = list[str]


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


#       PART ONE


def calculate_result_part_1(lines: list[str]) -> int:
    grid: Grid = [line.strip() for line in lines]
    rotated_grid = list(map("".join, zip(*grid)))

    tilted_grid = []
    for row in rotated_grid:
        rolled_rocks = []
        for group in row.split("#"):
            rolled = "".join(sorted(list(group), reverse=True))
            rolled_rocks.append(rolled)
        rolled_row = "#".join(rolled_rocks)
        tilted_grid.append(rolled_row)

    final_grid = list(map("".join, zip(*tilted_grid)))

    result: int = 0
    for i, row in enumerate(final_grid):
        rock_count = row.count("O")
        result += rock_count * (len(final_grid) - i)

    return result


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

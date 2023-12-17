import argparse

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Map = list[str]


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


def get_maps(lines: list[str]) -> list[Map]:
    maps: list[Map] = []
    current_map: Map = []

    for line in lines:
        if not line.strip():
            if current_map:
                maps.append(current_map)
                current_map = []
        else:
            current_map.append(line.strip())

    if current_map:
        maps.append(current_map)

    return maps


def get_mirror(map: Map) -> int:
    for y in range(1, len(map)):
        upper: Map = []
        for i in range(y - 1, -1, -1):
            upper.append(map[i])

        lower: Map = []
        for i in range(y, len(map)):
            lower.append(map[i])

        upper = upper[: len(lower)]
        lower = lower[: len(upper)]

        if upper == lower:
            return y
    return 0


def get_mirror_summary(map: Map) -> int:
    summary: int = 0

    mirror_row: int = get_mirror(map)
    summary += mirror_row * 100

    mirror_col: int = get_mirror(list(zip(*map)))
    summary += mirror_col

    return summary


#       PART ONE


def calculate_result_part_1(lines: list[str]) -> int:
    maps: list[Map] = get_maps(lines)
    result: list[int] = []

    for map in maps:
        result.append(get_mirror_summary(map))

    return sum(result)


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

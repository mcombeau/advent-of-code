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


def get_mirror(map: Map, isPart2: bool = False) -> int:
    for y in range(1, len(map)):
        upper: Map = []
        for i in range(y - 1, -1, -1):
            upper.append(map[i])

        lower: Map = []
        for i in range(y, len(map)):
            lower.append(map[i])

        upper = upper[: len(lower)]
        lower = lower[: len(upper)]

        if (not isPart2 and upper == lower) or (
            isPart2 and count_differences(upper, lower) == 1
        ):
            return y

    return 0


#       PART ONE


def calculate_result_part_1(lines: list[str]) -> int:
    maps: list[Map] = get_maps(lines)
    result: int = 0

    for map in maps:
        transposed_map = list(zip(*map))
        mirror_rows: int = get_mirror(map) * 100
        mirror_cols: int = get_mirror(transposed_map)
        result += mirror_rows + mirror_cols

    return result


#       PART TWO


def count_differences(upper: Map, lower: Map) -> int:
    difference_count: int = 0

    for row_upper, row_lower in zip(upper, lower):
        for a, b in zip(row_upper, row_lower):
            if a != b:
                difference_count += 1

    return difference_count


def calculate_result_part_2(lines: list[str]) -> int:
    maps: list[Map] = get_maps(lines)
    result: int = 0

    for map in maps:
        transposed_map = list(zip(*map))
        mirror_rows: int = get_mirror(map, isPart2=True) * 100
        mirror_cols: int = get_mirror(transposed_map, isPart2=True)
        result += mirror_rows + mirror_cols

    return result


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

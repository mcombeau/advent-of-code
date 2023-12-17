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


def calculate_result_part_1(line: str) -> int:
    sequences: tuple[str, ...] = tuple(line.split(","))
    result: int = 0

    for seq in sequences:
        current_value = 0
        for c in seq:
            current_value += ord(c)
            current_value *= 17
            current_value %= 256
        result += current_value

    return result


#       PART TWO


def calculate_result_part_2(line: str) -> int:
    return 0


#       MAIN


def main() -> None:
    args: Args = parse_args()
    with open(args.filename) as file:
        lines: list[str] = file.readlines()

    result: int = calculate_result_part_1(lines[0].strip())
    print(f"Part 1 Result: {result}")

    result: int = calculate_result_part_2(lines[0].strip())
    print(f"Part 2 Result: {result}")
    exit(0)


if __name__ == "__main__":
    main()

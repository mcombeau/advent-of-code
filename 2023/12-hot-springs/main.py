import argparse

Args = argparse.Namespace
Parser = argparse.ArgumentParser


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


#       PART ONE


def calculate_result_part_1(lines: list[str]) -> int:
    return 0


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

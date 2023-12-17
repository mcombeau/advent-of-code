import argparse
from functools import cache

Args = argparse.Namespace
Parser = argparse.ArgumentParser


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


#       PART ONE


def is_valid_group(record: str, group: int) -> bool:
    if group > len(record):
        return False

    contains_no_operational_gear = "." not in record[:group]
    not_followed_by_damaged_gear = group == len(record) or record[group] != "#"

    return (
        True if contains_no_operational_gear and not_followed_by_damaged_gear else False
    )


@cache
def get_number_arrangements(record: str, groups: tuple[int, ...]) -> int:
    if record == "":
        return 1 if groups == () else 0

    if groups == ():
        return 1 if not "#" in record else 0

    result: int = 0

    if record[0] in ".?":
        result += get_number_arrangements(record[1:], groups)

    if record[0] in "#?":
        if is_valid_group(record, groups[0]):
            result += get_number_arrangements(record[groups[0] + 1 :], groups[1:])
        else:
            result += 0

    return result


def calculate_result_part_1(lines: list[str]) -> int:
    total_arrangements: int = 0

    for line in lines:
        count: int = 0
        record, groups = line.split()
        groups = tuple(map(int, groups.split(",")))

        count += get_number_arrangements(record, groups)
        total_arrangements += count
        # print(f"{record:<20} {f'{groups}':<20} {count:<5}")

    return total_arrangements


#       PART TWO


def calculate_result_part_2(lines: list[str]) -> int:
    total_arrangements: int = 0

    for line in lines:
        count: int = 0

        record, groups = line.split()
        record = "?".join([record] * 5)

        groups = tuple(map(int, groups.split(",")))
        groups *= 5

        count += get_number_arrangements(record, groups)
        total_arrangements += count

    return total_arrangements


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

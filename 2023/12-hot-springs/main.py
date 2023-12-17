import argparse
from functools import cache
from enum import StrEnum

Args = argparse.Namespace
Parser = argparse.ArgumentParser


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


class gear(StrEnum):
    OPERATIONAL = "."
    DAMAGED = "#"
    UNKNOWN = "?"


#       PART ONE


def is_valid_group(record: str, group: int) -> bool:
    if group > len(record):
        return False

    return gear.OPERATIONAL not in record[:group] and (
        group == len(record) or record[group] != gear.DAMAGED
    )


@cache
def get_number_arrangements(record: str, groups: tuple[int, ...]) -> int:
    result: int = 0

    if record == "" or groups == ():
        result = (
            1 if groups == () and (record == "" or not gear.DAMAGED in record) else 0
        )
        return result

    if record[0] == gear.OPERATIONAL or record[0] == gear.UNKNOWN:
        result += get_number_arrangements(record[1:], groups)

    if (record[0] == gear.DAMAGED or record[0] == gear.UNKNOWN) and is_valid_group(
        record, groups[0]
    ):
        result += get_number_arrangements(record[groups[0] + 1 :], groups[1:])

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
        record = gear.UNKNOWN.join([record] * 5)

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

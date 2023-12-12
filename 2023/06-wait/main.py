import argparse
import typing
from functools import reduce

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Any = typing.Any


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


def get_nb_wins(race: tuple[int, int]) -> int:
    wins: int = 0
    time: int = race[0]
    distance: int = race[-1]

    for ms in range(1, time):
        finish_distance: int = ms * (time - ms)
        if finish_distance > distance:
            wins += 1

    return wins


#       PART ONE


def get_values(lines: list[str], index: int) -> list[int]:
    return [
        int(value)
        for value in lines[index].split(":")[-1].split(" ")
        if value.strip() != ""
    ]


def get_races(lines: list[str]) -> list[tuple[int, int]]:
    times: list[int] = get_values(lines, 0)
    distances: list[int] = get_values(lines, 1)

    return list(zip(times, distances))


def calculate_result_part_1(lines: list[str]) -> int:
    races: list[tuple[int, int]] = get_races(lines)
    wins: list[int] = []

    for race in races:
        nb_ways = get_nb_wins(race)
        wins.append(nb_ways)

    return reduce(lambda x, y: x * y, wins)


#       PART TWO


def get_value(lines: list[str], index: int) -> int:
    return int(
        "".join(
            [
                value
                for value in lines[index].split(":")[-1].split(" ")
                if value.strip() != ""
            ]
        )
    )


def get_race(lines: list[str]) -> tuple[int, int]:
    time: int = get_value(lines, 0)
    distance: int = get_value(lines, 1)

    return (time, distance)


def calculate_result_part_2(lines: list[str]) -> int:
    race: tuple[int, int] = get_race(lines)
    wins = get_nb_wins(race)

    return wins


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

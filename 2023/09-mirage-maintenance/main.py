import argparse
import numpy

Args = argparse.Namespace
Parser = argparse.ArgumentParser
History = list[list[int]]
Differences = list[list[int]]


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


def get_historical_values(lines: list[str]) -> History:
    history: History = []

    for line in lines:
        values: list[str] = line.split(" ")
        history.append([int(value) for value in values])

    return history


def does_list_contain_all_zeros(list_of_numbers: list[int]) -> bool:
    return all(n == 0 for n in list_of_numbers)


def get_difference(list_of_numbers: list[int]) -> list[int]:
    return list(numpy.diff(list_of_numbers))


def get_prediction(history: list[int]) -> int:
    differences: Differences = [history]

    i = 0
    while not does_list_contain_all_zeros(differences[i]):
        differences.append(get_difference(differences[i]))
        i += 1

    for i in range(len(differences) - 1, 0, -1):
        if i == len(differences) - 1:
            differences[i].append(0)
        else:
            differences[i - 1].append(differences[i][-1] + differences[i - 1][-1])

    return differences[0][-1]


#       PART ONE


def calculate_result_part_1(lines: list[str]) -> int:
    history: History = get_historical_values(lines)
    results: list[int] = []

    for hist in history:
        results.append(get_prediction(hist))

    return sum(results)


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

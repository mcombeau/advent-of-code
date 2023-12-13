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


def extrapolate_differences(history: list[int]) -> Differences:
    differences: Differences = [history]

    i = 0
    while not all(n == 0 for n in differences[i]):
        differences.append(list(numpy.diff(differences[i])))
        i += 1

    return differences


#       PART ONE


def get_future_prediction(history: list[int]) -> int:
    differences: Differences = extrapolate_differences(history)

    for i in range(len(differences) - 1, 0, -1):
        if i == len(differences) - 1:
            differences[i].append(0)
        else:
            differences[i - 1].append(differences[i][-1] + differences[i - 1][-1])

    return differences[0][-1]


def calculate_result_part_1(lines: list[str]) -> int:
    history: History = get_historical_values(lines)
    results: list[int] = []

    for hist in history:
        results.append(get_future_prediction(hist))

    return sum(results)


#       PART TWO


def get_past_prediction(history: list[int]) -> int:
    differences: Differences = extrapolate_differences(history)

    for i in range(len(differences) - 1, 0, -1):
        if i == len(differences) - 1:
            differences[i].insert(0, 0)
        else:
            differences[i - 1].insert(0, differences[i - 1][0] - differences[i][0])

    return differences[0][0]


def calculate_result_part_2(lines: list[str]) -> int:
    history: History = get_historical_values(lines)
    results: list[int] = []

    for hist in history:
        results.append(get_past_prediction(hist))

    return sum(results)


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

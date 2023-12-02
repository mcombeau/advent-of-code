import re
import argparse
import typing

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Pattern = re.Pattern[str]
Any = typing.Any

def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()
    return args

def calculate_result_part_1(lines: list[str]) -> int :
    numbers: list[int] = []
    for line in lines:
        digits: list[str] = re.findall(r"\d", line)
        if (len(digits) > 0):
            numbers.append((int(digits[0]) * 10) + int(digits[-1]))

    result: int = sum(numbers)
    return result

def get_numbers_from_line(line: str, pattern: Pattern, words: list[str]) -> int:
    matches: Any = re.finditer(pattern, line)
    numbers: list[Any] = []
    for match in matches:
        for group in match.groups():
            if (group is not None and group != ""): numbers.append(group)
    numbers: list[Any] = [int(num) if num.isdigit() else words.index(num) + 1 for num in numbers]
    if (len(numbers) > 0):
        return numbers[0] * 10 + numbers[-1]
    return 0


def calculate_result_part_2(lines: list[str]) -> int :
    words: list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    pattern: Pattern = re.compile(r"(?=(\d))|(?=(" + "))|(?=(".join(words) + "))")
    res: list[int] = []
    for line in lines:
        res.append(get_numbers_from_line(line, pattern, words))
    result: int = sum(res)
    return result

def main() -> None:
    args: Args = parse_args()
    with open(args.filename) as file:
        lines : list[str] = file.readlines();
    result: int = calculate_result_part_1(lines)
    print(f"Part 1 Result: {result}")

    result: int = calculate_result_part_2(lines)
    print(f"Part 2 Result: {result}")
    exit(0)

if __name__ == "__main__":
    main()


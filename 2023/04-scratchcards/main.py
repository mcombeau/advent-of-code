import argparse
import typing

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Any = typing.Any

def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()
    return args

def get_winning_numbers(card: str) -> list[int]:
    strings: list[str] = card.strip().split(":")[1].split("|")[0].strip().split(' ')
    strings: list[str] = list(filter(None, strings))
    numbers: list[int] = [int(num) for num in strings]
    return numbers

def get_my_numbers(card: str) -> list[int]:
    strings: list[str]  = card.strip().split(":")[1].split("|")[1].strip().split(' ')
    strings: list[str] = list(filter(None, strings))
    numbers: list[int] = [int(num) for num in strings]
    return numbers


#       PART ONE

def get_card_point_value(winning_numbers: list[int], my_numbers: list[int]) -> int:
    matching_numbers: set[int] = set(winning_numbers).intersection(my_numbers)
    points: int = 0
    for match in matching_numbers:
        if points == 0:
            points += 1
        else:
            points += points
    return points

def calculate_result_part_1(cards: list[str]) -> int :
    points: list[int] = []
    for card in cards:
        winning_numbers: list[int] = get_winning_numbers(card)
        my_numbers: list[int] = get_my_numbers(card)
        points.append(get_card_point_value(winning_numbers, my_numbers))
    return sum(points)


#       PART TWO
#   This solution works but is extremely inefficient ! :D

def add_to_card_total(card_id: int, cards_total: dict[int, int], number_matches: int) -> None:
    for i in range(0, number_matches):
        cards_total[card_id + i + 1] += 1
    return

def calculate_result_part_2(cards: list[str]) -> int :

    cards_total: dict[int, int] = {}
    for i, card in enumerate(cards): cards_total[i + 1] = 1 
    for i, card in enumerate(cards):
        for x in range(0, cards_total[i + 1]):
            winning_numbers: list[int] = get_winning_numbers(card)
            my_numbers: list[int] = get_my_numbers(card)
            matching_numbers: set[int] = set(winning_numbers).intersection(my_numbers)
            add_to_card_total(i + 1, cards_total, len(matching_numbers))
    return sum(cards_total.values())


#       MAIN

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


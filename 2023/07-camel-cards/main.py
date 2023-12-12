import argparse
import typing
from enum import Enum

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Any = typing.Any


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


class HandType(Enum):
    FIVE_OF_KIND = 1
    FOUR_OF_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7
    ERROR = 0


class Hand:
    def __init__(self, cards: str, bid: int, hand_type: HandType):
        self = self
        self.cards = cards
        self.bid = bid
        self.hand_type = hand_type
        self.rank = 0


def get_card_numbers(cards: str) -> dict[str, int]:
    valid_cards: str = "AKQJT98765432"
    card_numbers: dict[str, int] = {}
    for card in valid_cards:
        card_numbers[card] = 0
    for card in cards:
        card_numbers[card] += 1
    return card_numbers


def get_full_house_or_three_of_kind(card_numbers: dict[str, int]) -> HandType:
    for number in card_numbers.values():
        if number == 2:
            return HandType.FULL_HOUSE
    return HandType.THREE_OF_KIND


def get_two_or_one_pair(card_numbers: dict[str, int]) -> HandType:
    num_pairs = 0
    for number in card_numbers.values():
        if number == 2:
            num_pairs += 1
    if num_pairs == 2:
        return HandType.TWO_PAIR
    return HandType.ONE_PAIR


def get_hand_type(cards: str) -> HandType:
    card_numbers: dict[str, int] = get_card_numbers(cards)
    highest_number_of_same_cards: int = 0
    for number in card_numbers.values():
        if number > highest_number_of_same_cards:
            highest_number_of_same_cards = number

    match highest_number_of_same_cards:
        case 5:
            return HandType.FIVE_OF_KIND
        case 4:
            return HandType.FOUR_OF_KIND
        case 1:
            return HandType.HIGH_CARD
        case 3:
            return get_full_house_or_three_of_kind(card_numbers)
        case 2:
            return get_two_or_one_pair(card_numbers)
    return HandType.ERROR


def get_hands(lines: list[str]) -> list[Hand]:
    hands: list[Hand] = []
    for line in lines:
        cards: str = line.split(" ")[0]
        bid: int = int(line.split(" ")[-1])
        hand_type: HandType = get_hand_type(cards)
        hands.append(Hand(cards, bid, hand_type))

    return hands


#       PART ONE


def get_card_values() -> dict[str, int]:
    valid_cards: str = "AKQJT98765432"
    card_values: dict[str, int] = {}
    for i, card in enumerate(valid_cards):
        card_values[card] = len(valid_cards) - i - 1
    print(f"Card values: {card_values}")
    return card_values


def should_switch_ranks(
    card_values: dict[str, int], current_hand: Hand, hand: Hand
) -> bool:
    return False


def assign_ranks(hands: list[Hand]) -> list[Hand]:
    card_values: dict[str, int] = get_card_values()
    sorted_hands: list[Hand] = sorted(
        hands, key=lambda x: x.hand_type.value, reverse=True
    )
    for i, hand in enumerate(sorted_hands):
        hand.rank = i + 1
        print(
            f"Hand: cards: {hand.cards}, bid: {hand.bid}, type: {hand.hand_type}, rank: {hand.rank}"
        )
    for i, current_hand in enumerate(sorted_hands):
        for j, hand in enumerate(sorted_hands):
            if i == j:
                continue
            if current_hand.hand_type != hand.hand_type:
                continue
            if should_switch_ranks(card_values, current_hand, hand):
                tmp: int = current_hand.rank
                current_hand.rank = hand.rank
                hand.rank = current_hand.rank
                i = 0
                break

            # determine if we need to switch ranks
    return sorted_hands


def calculate_result_part_1(lines: list[str]) -> int:
    hands: list[Hand] = get_hands(lines)
    ranked_hands: list[Hand] = assign_ranks(hands)

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

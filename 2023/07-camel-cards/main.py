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


def get_hands(lines: list[str], isPart2: bool) -> list[Hand]:
    hands: list[Hand] = []
    for line in lines:
        cards: str = line.split(" ")[0]
        bid: int = int(line.split(" ")[-1])
        if isPart2:
            hand_type: HandType = get_hand_type_part2(cards)
        else:
            hand_type: HandType = get_hand_type(cards)
        hands.append(Hand(cards, bid, hand_type))

    return hands


#       PART ONE


def assign_ranks(hands: list[Hand]) -> list[Hand]:
    sorted_hands_by_cards: list[Hand] = sorted(hands, key=lambda x: x.cards)
    # for hand in sorted_hands_by_cards:
    #     print(f"Hand: cards: {hand.cards}, type: {hand.hand_type}")
    sorted_hands_by_type: list[Hand] = sorted(
        sorted_hands_by_cards, key=lambda x: x.hand_type.value, reverse=True
    )
    for i, hand in enumerate(sorted_hands_by_type):
        hand.rank = i + 1

    return sorted_hands_by_type


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


def calculate_result_part_1(lines: list[str]) -> int:
    hands: list[Hand] = get_hands(lines, isPart2=False)
    for hand in hands:
        hand.cards = (
            hand.cards.replace("A", "Z")
            .replace("K", "Y")
            .replace("Q", "X")
            .replace("J", "W")
            .replace("T", "V")
        )
    ranked_hands: list[Hand] = assign_ranks(hands)
    result = 0

    for hand in ranked_hands:
        result += hand.bid * hand.rank

    return result


#       PART TWO

# Full house: 23332, where three cards have the same label, and the remaining two cards share a different label:
# Three of a kind: TTT98, where three cards have the same label, and the remaining two cards are each different from any other card in the hand:

# 2J233 -> Labeled THREE OF KIND when it is FULL HOUSE

# 12767 -> Labeled FULL HOUSE when is THREE OF KIND


def get_full_house_or_three_of_kind_part2(card_numbers: dict[str, int]) -> HandType:
    nb_jokers = card_numbers["J"]

    if nb_jokers == 0:
        # default to part 1 if no jokers
        return get_full_house_or_three_of_kind(card_numbers)

    highest_number = 0
    nb_pairs = 0
    for card, number in card_numbers.items():
        if not card == "J":
            if number == 2:
                nb_pairs += 1
            if number > highest_number:
                highest_number = number

    if highest_number == 2 and nb_pairs == 2 and nb_jokers >= 1:
        return HandType.FULL_HOUSE

    return HandType.THREE_OF_KIND


def get_two_or_one_pair_part2(card_numbers: dict[str, int]) -> HandType:
    nb_jokers = card_numbers["J"]

    if nb_jokers == 0:
        # default to part 1 if no jokers
        return get_two_or_one_pair(card_numbers)

    return HandType.ONE_PAIR


def get_hand_type_part2(cards: str) -> HandType:
    card_numbers: dict[str, int] = get_card_numbers(cards)
    nb_jokers = card_numbers["J"]
    highest_number_of_same_cards: int = 0

    for card, number in card_numbers.items():
        if not card == "J" and number > highest_number_of_same_cards:
            highest_number_of_same_cards = number

    if highest_number_of_same_cards == 0 and nb_jokers == 5:
        return HandType.FIVE_OF_KIND

    highest_number_of_same_cards += nb_jokers

    match highest_number_of_same_cards:
        case 5:
            return HandType.FIVE_OF_KIND
        case 4:
            return HandType.FOUR_OF_KIND
        case 1:
            return HandType.HIGH_CARD
        case 3:
            return get_full_house_or_three_of_kind_part2(card_numbers)
        case 2:
            return get_two_or_one_pair_part2(card_numbers)
    return HandType.ERROR


def calculate_result_part_2(lines: list[str]) -> int:
    hands: list[Hand] = get_hands(lines, isPart2=True)
    # for hand in hands:
    #     print(f"Hand: cards: {hand.cards}, type: {hand.hand_type}")
    for hand in hands:
        hand.cards = (
            hand.cards.replace("A", "Z")
            .replace("K", "Y")
            .replace("Q", "X")
            .replace("T", "V")
            .replace("J", "1")
        )
    ranked_hands: list[Hand] = assign_ranks(hands)
    result = 0

    print("-" * 20)
    for hand in ranked_hands:
        print(
            f"Hand: cards: {hand.cards}, type: {hand.hand_type}, bid: {hand.bid}, rank: {hand.rank}"
        )
        result += hand.bid * hand.rank
    return result


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

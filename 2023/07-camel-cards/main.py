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


def count_cards(cards: str) -> dict[str, int]:
    valid_cards: str = "AKQJT98765432"
    card_count: dict[str, int] = {}

    for card in valid_cards:
        card_count[card] = 0

    for card in cards:
        card_count[card] += 1

    return card_count


def get_hands(lines: list[str], isPart2: bool) -> list[Hand]:
    hands: list[Hand] = []

    for line in lines:
        cards: str = line.split(" ")[0]
        bid: int = int(line.split(" ")[-1])
        hand_type: HandType = get_hand_type(cards, isPart2)
        hands.append(Hand(cards, bid, hand_type))

    return hands


def assign_ranks(hands: list[Hand]) -> list[Hand]:
    sorted_hands_by_cards: list[Hand] = sorted(hands, key=lambda x: x.cards)
    sorted_hands_by_type: list[Hand] = sorted(
        sorted_hands_by_cards, key=lambda x: x.hand_type.value, reverse=True
    )

    for i, hand in enumerate(sorted_hands_by_type):
        hand.rank = i + 1

    return sorted_hands_by_type


def get_full_house_or_three_of_kind(
    card_count: dict[str, int], isPart2: bool
) -> HandType:
    if not isPart2 or (isPart2 and card_count["J"] == 0):
        for count in card_count.values():
            if count == 2:
                return HandType.FULL_HOUSE
        return HandType.THREE_OF_KIND

    highest_count = 0
    pair_count = 0
    for card, count in card_count.items():
        if not card == "J":
            if count == 2:
                pair_count += 1
            if count > highest_count:
                highest_count = count

    if highest_count == 2 and pair_count == 2 and card_count["J"] >= 1:
        return HandType.FULL_HOUSE

    return HandType.THREE_OF_KIND


def get_two_or_one_pair(card_count: dict[str, int], isPart2: bool) -> HandType:
    if isPart2 and card_count["J"] >= 1:
        return HandType.ONE_PAIR

    pair_count = 0
    for count in card_count.values():
        if count == 2:
            pair_count += 1

    if pair_count == 2:
        return HandType.TWO_PAIR

    return HandType.ONE_PAIR


def get_hand_type(cards: str, isPart2: bool) -> HandType:
    card_count: dict[str, int] = count_cards(cards)
    highest_card_count: int = 0

    for card, count in card_count.items():
        if not card == "J" and count > highest_card_count:
            highest_card_count = count

    if isPart2:
        highest_card_count += card_count["J"]
    else:
        if card_count["J"] > highest_card_count:
            highest_card_count = card_count["J"]

    match highest_card_count:
        case 5:
            return HandType.FIVE_OF_KIND
        case 4:
            return HandType.FOUR_OF_KIND
        case 1:
            return HandType.HIGH_CARD
        case 3:
            return get_full_house_or_three_of_kind(card_count, isPart2)
        case 2:
            return get_two_or_one_pair(card_count, isPart2)
    return HandType.ERROR


#       PART ONE


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

    result: int = 0
    for hand in ranked_hands:
        result += hand.bid * hand.rank

    return result


#       PART TWO


def calculate_result_part_2(lines: list[str]) -> int:
    hands: list[Hand] = get_hands(lines, isPart2=True)

    for hand in hands:
        hand.cards = (
            hand.cards.replace("A", "Z")
            .replace("K", "Y")
            .replace("Q", "X")
            .replace("T", "V")
            .replace("J", "1")
        )

    ranked_hands: list[Hand] = assign_ranks(hands)

    result: int = 0
    for hand in ranked_hands:
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

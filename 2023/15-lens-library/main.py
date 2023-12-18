import argparse

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Box = list[tuple[str, int]]


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


def decode_value(code: str) -> int:
    current_value = 0

    for c in code:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256

    return current_value


#       PART ONE


def calculate_result_part_1(line: str) -> int:
    sequences: tuple[str, ...] = tuple(line.split(","))
    result: int = 0

    for sequence in sequences:
        result += decode_value(sequence)

    return result


#       PART TWO


def get_lens_info(sequence: str) -> tuple[str, int, int]:
    label: str = sequence.split("=")[0] if "=" in sequence else sequence[:-1]
    focal_length: int = int(sequence.split("=")[-1]) if "=" in sequence else -1
    box_index: int = decode_value(label)

    return (label, focal_length, box_index)


def add_lens_to_box(box: Box, label: str, focal_length: int) -> None:
    replaced_lens: bool = False

    for i, lens in enumerate(box):
        if lens[0] == label:
            box[i] = (label, focal_length)
            replaced_lens = True
            break

    if replaced_lens == False:
        box.append((label, focal_length))


def remove_lens_from_box(box: Box, label: str) -> None:
    for i, lens in enumerate(box):
        if lens[0] == label:
            box.pop(i)
            break


def calculate_result_part_2(line: str) -> int:
    sequences: tuple[str, ...] = tuple(line.split(","))
    boxes: list[Box] = [[] for _ in range(256)]

    for sequence in sequences:
        label, focal_length, box_index = get_lens_info(sequence)

        if "-" in sequence:
            remove_lens_from_box(boxes[box_index], label)

        elif "=" in sequence:
            add_lens_to_box(boxes[box_index], label, focal_length)

    result: int = 0
    for b, box in enumerate(boxes):
        for l, lens in enumerate(box):
            result += (b + 1) * (l + 1) * lens[-1]

    return result


#       MAIN


def main() -> None:
    args: Args = parse_args()
    with open(args.filename) as file:
        lines: list[str] = file.readlines()

    result: int = calculate_result_part_1(lines[0].strip())
    print(f"Part 1 Result: {result}")

    result: int = calculate_result_part_2(lines[0].strip())
    print(f"Part 2 Result: {result}")
    exit(0)


if __name__ == "__main__":
    main()

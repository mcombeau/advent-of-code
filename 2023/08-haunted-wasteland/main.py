import argparse
import math

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Map = dict[str, tuple[str, str]]


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


def get_map(lines: list[str]) -> Map:
    map: Map = {}
    for line in lines:
        if not "=" in line:
            continue
        node: str = line.strip().split("=")[0].strip()
        dirs: list[str] = (
            line.strip().split("=")[-1].replace("(", "").replace(")", "").split(",")
        )
        map[node] = (dirs[0].strip(), dirs[-1].strip())

    return map


def navigate_directions(starting_pos: str, directions: str, map: Map) -> str:
    current_pos: str = starting_pos

    for dir in directions:
        fork: int = 0 if dir == "L" else 1
        current_pos = map[current_pos][fork]

    return current_pos


#       PART ONE


def calculate_result_part_1(lines: list[str]) -> int:
    directions: str = lines[0].strip()
    map: Map = get_map(lines)
    pos: str = "AAA"
    steps: int = 0

    while pos != "ZZZ":
        pos = navigate_directions(pos, directions, map)
        steps += len(directions)

    return steps


#       PART TWO


def init_pos_steps(map: Map) -> dict[str, int]:
    pos_steps: dict[str, int] = {}

    for pos in map.keys():
        if pos[-1] == "A":
            pos_steps[pos] = 0

    return pos_steps


def calculate_result_part_2(lines: list[str]) -> int:
    directions: str = lines[0].strip()
    map: Map = get_map(lines)
    pos_steps: dict[str, int] = init_pos_steps(map)

    for initial_pos in pos_steps:
        current_pos: str = initial_pos

        while current_pos[-1] != "Z":
            current_pos = navigate_directions(current_pos, directions, map)
            pos_steps[initial_pos] += len(directions)

    return math.lcm(*pos_steps.values())


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

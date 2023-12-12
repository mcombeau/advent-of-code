import argparse
import sys

Args = argparse.Namespace
Parser = argparse.ArgumentParser


def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()

    return args


def get_seed_numbers(lines: list[str]) -> list[int]:
    seedStr: list[str] = lines[0].strip().split(":")[1].strip().split(" ")

    return [int(i) for i in seedStr]


#        PART ONE


def get_maps(lines: list[str]) -> list[dict[range, range]]:
    maps: list[dict[range, range]] = []

    for line in lines[2:]:
        if "map" in line:
            maps.append({})
        elif line.strip() != "":
            values: list[str] = line.strip().split(" ")
            source: int = int(values[1])
            destination: int = int(values[0])
            length: int = int(values[2])
            maps[-1][range(source, source + length)] = range(
                destination, destination + length
            )

    return maps


def get_location_from_seed(seed: int, maps: list[dict[range, range]]) -> int:
    loc: int = seed

    for current_map in maps:
        for source, destination in current_map.items():
            if loc in source:
                loc = destination.start + (loc - source.start)
                break

    return loc


def calculate_result_part_one(lines: list[str]) -> int:
    seeds: list[int] = get_seed_numbers(lines)
    maps: list[dict[range, range]] = get_maps(lines)
    lowest_location: int = sys.maxsize

    for seed in seeds:
        loc: int = get_location_from_seed(seed, maps)
        if loc < lowest_location:
            lowest_location = loc

    return lowest_location


#        PART TWO


def get_seed_ranges(lines: list[str]) -> list[range]:
    seeds: list[int] = get_seed_numbers(lines)
    seed_ranges: list[range] = []

    for i in range(0, len(seeds), 2):
        start: int = seeds[i]
        end: int = seeds[i] + seeds[i + 1] - 1
        seed_ranges.append(range(start, end))

    return seed_ranges


def get_seed_from_location(loc: int, maps: list[dict[range, range]]) -> int:
    seed = loc
    for current_map in reversed(maps):
        for source, destination in current_map.items():
            if seed in destination:
                seed = source.start + (seed - destination.start)
                break
    return seed


def calculate_result_part_two(lines: list[str]) -> int:
    seed_ranges: list[range] = get_seed_ranges(lines)
    maps: list[dict[range, range]] = get_maps(lines)

    lowest_location = -1

    while True:
        lowest_location += 1
        seed_candidate = get_seed_from_location(lowest_location, maps)
        print(f"Testing location: {lowest_location}", end="\r")
        for seed_range in seed_ranges:
            if seed_candidate in seed_range:
                return lowest_location


#        MAIN


def main() -> None:
    args: Args = parse_args()
    lines: list[str] = []
    with open(args.filename) as file:
        lines: list[str] = file.readlines()
    print("PART ONE")
    print("-" * 40)
    result: int = calculate_result_part_one(lines)
    print(f"Part 1 Result: {result}")
    print("-" * 40, end="\n\n")
    print("PART TWO")
    print("-" * 40)
    print(f"Processing...", end="\n")
    result: int = calculate_result_part_two(lines)
    print()
    print("-" * 40)
    print(f"Part 2 Result: {result}")
    print("-" * 40)
    exit(0)


if __name__ == "__main__":
    main()

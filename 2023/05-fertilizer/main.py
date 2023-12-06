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

def get_seed_numbers(lines: list[str]) -> list[int]:
    seedStr: list[str] = lines[0].strip().split(":")[1].strip().split(" ")
    return [int(i) for i in seedStr]

def get_map(lines: list[str], title: str) -> list[tuple[int, int, int]]:
    save_next_lines: bool = False
    saved_map: list[tuple[int, int, int]] = []
    for line in lines:
        if line.startswith(title):
            save_next_lines: bool = True
            continue
        if save_next_lines and not line.strip():
            break
        elif save_next_lines:
            elements: list[str] = line.strip().split(" ")
            saved_map.append((int(elements[0]), int(elements[1]), int(elements[2])))
    return saved_map

def get_correspondance(source: int, map: list[tuple[int, int, int]]) -> int:
    for m in map:
        min_range: int = m[1]
        max_range: int = m[1] + m[2]
        if source in range(min_range, max_range):
            offset:int = source - min_range
            return m[0] + offset
    return source

def get_lowest_seed_location(lines: list[str], seeds: list[int]) -> int:
    seed_soil_map: list[tuple[int, int, int]] = get_map(lines, "seed-to-soil")
    soil_fert_map: list[tuple[int, int, int]] = get_map(lines, "soil-to-fertilizer")
    fert_water_map: list[tuple[int, int, int]] = get_map(lines, "fertilizer-to-water")
    water_light_map: list[tuple[int, int, int]] = get_map(lines, "water-to-light")
    light_temp_map: list[tuple[int, int, int]] = get_map(lines, "light-to-temperature")
    temp_humid_map: list[tuple[int, int, int]] = get_map(lines, "temperature-to-humidity")
    humid_loc_map: list[tuple[int, int, int]] = get_map(lines, "humidity-to-location")

    locations: list[int] = []
    for seed in seeds:
        num: int = get_correspondance(seed, seed_soil_map)
        num: int = get_correspondance(num, soil_fert_map)
        num: int = get_correspondance(num, fert_water_map)
        num: int = get_correspondance(num, water_light_map)
        num: int = get_correspondance(num, light_temp_map)
        num: int = get_correspondance(num, temp_humid_map)
        num: int = get_correspondance(num, humid_loc_map)
        locations.append(num)
    return min(loc for loc in locations)

def calculate_result_part_one(lines: list[str]) -> int :
    seeds: list[int] = get_seed_numbers(lines)
    return get_lowest_seed_location(lines, seeds)

# TODO: FIX THIS IT KILLS MY COMPUTER :(
def process_seed_chunk(min_range, max_range, lines: list[str]) -> int:
    seeds: list[int] = []
    [seeds.append(s) for s in range(min_range, max_range)]
    print(f"made seed list: {seeds}")
    return get_lowest_seed_location(lines, seeds)

def calculate_result_part_two(lines: list[str]) -> int:
    seed_numbers: list[int] = get_seed_numbers(lines)
    for i, seed in enumerate(seed_numbers):
        min_range: int = seed
        max_range: int = min_range + seed_numbers[i + 1]
        lowest_loc: int = process_seed_chunk(min_range, max_range, lines)
        print(f"Lowest location for chunk: {lowest_loc}")
        seed_numbers.remove(seed)
    return 0

def main() -> None:
    args: Args = parse_args()
    lines: list[str] = []
    with open(args.filename) as file:
        lines : list[str] = file.readlines();
    result: int = calculate_result_part_one(lines)
    print(f"Part 1 Result: {result}")

    # TODO: FIX PART TWO
    result: int = calculate_result_part_two(lines)
    print(f"Part 2 Result: {result}")
    exit(0)

if __name__ == "__main__":
    main()


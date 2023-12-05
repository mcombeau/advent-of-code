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

def get_seed_numbers(lines: list[str]) -> list[int]:
    seedstr: list[str] = lines[0].strip().split(":")[1].strip().split(" ")
    seeds: list[int] = [int(i) for i in seedstr]
    return seeds

def get_map_after_title(lines: list[str], title: str) -> list[str]:
    save_next_lines: bool = False
    saved_map: list[str] = []
    for line in lines:
        if line.startswith(title):
            save_next_lines: bool = True
            continue
        if save_next_lines and not line.strip():
            break
        elif save_next_lines:
            saved_map.append(line)
    return saved_map

def get_seed_to_soil_map(lines: list[str]):
    seed_to_soil_map: list[str] = get_map_after_title(lines, "seed-to-soil")
    print("Seed to soil map = ", seed_to_soil_map)
    soil_to_fertilizer_map: list[str] = get_map_after_title(lines, "soil-to-fertilizer")
    print("Seed to soil map = ", soil_to_fertilizer_map)
    fertilizer_to_water_map: list[str] = get_map_after_title(lines, "fertilizer-to-water")
    print("Seed to soil map = ", fertilizer_to_water_map)
    water_to_light_map: list[str] = get_map_after_title(lines, "water-to-light")
    print("Seed to soil map = ", water_to_light_map)
    light_to_temperature_map: list[str] = get_map_after_title(lines, "light-to-temperature")
    print("Seed to soil map = ", light_to_temperature_map)
    temperature_to_humidity_map: list[str] = get_map_after_title(lines, "temperature-to-humidity")
    print("Seed to soil map = ", temperature_to_humidity_map)
    humidity_to_location_map: list[str] = get_map_after_title(lines, "humidity-to-location")
    print("Seed to soil map = ", humidity_to_location_map)
    return

def calculate_result_part_1(lines: list[str]) -> int :
    seeds: list[int] = get_seed_numbers(lines)
    get_seed_to_soil_map(lines)
    
    return 0

def calculate_result_part_2(lines: list[str]) -> int :
    return 0

def main() -> None:
    args: Args = parse_args()
    lines: list[str] = []
    with open(args.filename) as file:
        lines : list[str] = file.readlines();
    print("----- INPUT ------")
    [print(line, end="") for line in lines]
    print("--- END INPUT ----")
    print()
    result: int = calculate_result_part_1(lines)
    print(f"Part 1 Result: {result}")

    result: int = calculate_result_part_2(lines)
    print(f"Part 2 Result: {result}")
    exit(0)

if __name__ == "__main__":
    main()


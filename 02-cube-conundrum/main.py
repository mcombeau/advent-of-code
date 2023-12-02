import re
import argparse
import typing
from enum import Enum

Args = argparse.Namespace
Parser = argparse.ArgumentParser
Pattern = re.Pattern[str]
Any = typing.Any

def parse_args() -> Args:
    parser: Parser = Parser()
    parser.add_argument("filename")
    args: Args = parser.parse_args()
    return args

def get_game_id(line: str) -> int:
    return int(line.split(":")[0].split(' ')[-1])

def get_sub_games(line: str) -> list[str]:
    return line.strip().split(':')[-1].split(";")

def get_game_rgb(s: str) -> dict[str, int]:
    colors: dict[str, int] = {'red':0, 'green':0, 'blue':0}
    cubes: list[str] = s.split(',')
    for c in cubes:
        cube: list[str] = c.strip().split(' ')
        match cube[-1]:
            case 'red':
                colors['red'] = int(cube[0])
            case 'green':
                colors['green'] = int(cube[0])
            case 'blue':
                colors['blue'] = int(cube[0])
    return colors


# ----------  PART I

def evaluate_game_session(max_cubes: dict[str, int], line: str) -> int:
    game_id: int = get_game_id(line)
    sub_games: list[str] = get_sub_games(line)
    for game in sub_games:
        rgb: dict[str, int] = get_game_rgb(game)
        if (rgb['red'] > max_cubes['red']
                or rgb['green'] > max_cubes['green']
                or rgb['blue'] > max_cubes['blue']):
            raise Exception("invalid game")
    return game_id


def calculate_result_part_1(lines: list[str]) -> int :
    print("----- PART I")
    max_cubes: dict[str, int] = {'red':12, 'green':13, 'blue':14}
    print(f"Max number of cubes: red = {max_cubes['red']}, green = {max_cubes['green']}, blue = {max_cubes['blue']}")
    valid_games: list[int] = []
    for line in lines:
        try:
            game_id: int = evaluate_game_session(max_cubes, line)
            valid_games.append(game_id)
        except:
            continue
    print("Valid Games:", valid_games)
    return sum(valid_games)


# ----------  PART II
def get_min_cubes_for_game(line: str) -> dict[str, int]:
    min_cubes: dict[str, int] = {'red':0, 'green':0, 'blue':0}
    sub_games: list[str] = get_sub_games(line)
    for game in sub_games:
        game_cubes: dict[str, int] = get_game_rgb(game)
        if min_cubes['red'] < game_cubes['red']:
            min_cubes['red'] = game_cubes['red']
        if min_cubes['green'] < game_cubes['green']:
            min_cubes['green'] = game_cubes['green']
        if min_cubes['blue'] < game_cubes['blue']:
            min_cubes['blue'] = game_cubes['blue']
    return min_cubes

def calculate_result_part_2(lines: list[str]) -> int:
    print("----- PART II")
    power_cubes: list[int] = []
    for line in lines:
        min_cubes: dict[str, int] = get_min_cubes_for_game(line)
        power_cubes.append(min_cubes['red'] * min_cubes['green'] * min_cubes['blue'])
    print(f"Powers of cubes for each game: {power_cubes}")
    return sum(power_cubes)


# ----------  MAIN

def main() -> None:
    args: Args = parse_args()
    with open(args.filename) as file:
        lines : list[str] = file.readlines();
    result: int = calculate_result_part_1(lines)
    print(f"Result: {result}\n")
    result: int = calculate_result_part_2(lines)
    print(f"Result: {result}\n")
    exit(0)

if __name__ == "__main__":
    main()


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

def print_grid(grid: list[str]) -> None:
    for y, row in enumerate(grid):
        for x in range(0, len(row)):
            print(grid[y][x], end="")
    print()


#       PART ONE

def is_special_character(c: str) -> bool:
    return False if re.match(r"[^\.^\d^\n]", c) == None else True

def check_row_above(grid: list[str], y: int, x: int) -> bool:
    if y < 0: return False
    if is_special_character(grid[y - 1][x]): return True
    if is_special_character(grid[y - 1][x + 1]): return True
    if x > 0 and is_special_character(grid[y - 1][x - 1]): return True
    return False

def check_same_row(grid: list[str], y: int, x: int) -> bool:
    if is_special_character(grid[y][x + 1]): return True
    if x > 0 and is_special_character(grid[y][x - 1]): return True
    return False

def check_row_below(grid: list[str], y: int, x: int) -> bool:
    if y >= len(grid) - 1: return False
    if is_special_character(grid[y + 1][x]): return True
    if is_special_character(grid[y + 1][x + 1]): return True
    if x > 0 and is_special_character(grid[y + 1][x - 1]): return True
    return False

def is_num_touching_special_char(grid: list[str], y: int, x: int) -> bool:
    if check_same_row(grid, y, x): return True
    if check_row_above(grid, y, x): return True
    if check_row_below(grid, y, x): return True
    return False

def save_number(grid: list[str], y: int, x: int, numbers: list[int]) -> int:
    should_save_number: bool = False
    start_index: int = x
    end_index: int = 0
    for i in range(x, len(grid[y])):
        if not grid[y][i].isdigit():
            end_index = i
            break
        if should_save_number is False:
            should_save_number = is_num_touching_special_char(grid, y, i)
    if should_save_number:
        numbers.append(int(grid[y][start_index:end_index]))
    return end_index - start_index

def calculate_result_part_1(grid: list[str]) -> int :
    numbers: list[int] = []
    for y, row in enumerate(grid):
        x: int = 0
        while x < len(row):
            if grid[y][x].isdigit():
                x += save_number(grid, y, x, numbers)
            else:
                x += 1
    return sum(numbers)

#       PART TWO

def is_gear(c: str) -> bool:
    return False if re.match(r"\*", c) == None else True

def get_number_at_grid_pos(grid: list[str], y: int, x: int) -> int:
    start_index: int = x
    end_index: int = x
    for i in range(x, -1, -1):
        if i == 0:
            start_index = i
        if not grid[y][i].isdigit():
            start_index = i + 1
            break
    for i in range(x + 1, len(grid[y])):
        if i == len(grid[y]) - 1:
            end_index = i
        if not grid[y][i].isdigit():
            end_index = i
            break
    return int(grid[y][start_index:end_index])

def find_number_above_center(grid: list[str], y: int, x: int) -> int:
    if y < 0: return -1
    if grid[y - 1][x].isdigit(): return get_number_at_grid_pos(grid, y - 1, x)
    return -1

def find_number_above_left(grid: list[str], y: int, x: int) -> int:
    if y < 0 or grid[y - 1][x].isdigit(): return -1
    if x > 0 and grid[y - 1][x - 1].isdigit(): return get_number_at_grid_pos(grid, y - 1, x - 1)
    return -1

def find_number_above_right(grid: list[str], y: int, x: int) -> int:
    if y < 0 or grid[y - 1][x].isdigit(): return -1
    if grid[y - 1][x + 1].isdigit(): return get_number_at_grid_pos(grid, y - 1, x + 1)
    return -1

def find_number_left(grid: list[str], y: int, x: int) -> int:
    if x > 0 and grid[y][x - 1].isdigit(): return get_number_at_grid_pos(grid, y, x - 1)
    return -1

def find_number_right(grid: list[str], y: int, x: int) -> int:
    if grid[y][x + 1].isdigit(): return get_number_at_grid_pos(grid, y, x + 1)
    return -1

def find_number_below_center(grid: list[str], y: int, x: int) -> int:
    if y >= len(grid) - 1: return -1
    if grid[y + 1][x].isdigit(): return get_number_at_grid_pos(grid, y + 1, x)
    return -1

def find_number_below_left(grid: list[str], y: int, x: int) -> int:
    if y < 0 or grid[y + 1][x].isdigit(): return -1
    if x > 0 and grid[y + 1][x - 1].isdigit(): return get_number_at_grid_pos(grid, y + 1, x - 1)
    return -1

def find_number_below_right(grid: list[str], y: int, x: int) -> int:
    if y < 0 or grid[y + 1][x].isdigit(): return -1
    if grid[y + 1][x + 1].isdigit(): return get_number_at_grid_pos(grid, y + 1, x + 1)
    return -1

def save_gear_ratio(grid: list[str], y: int, x: int, ratios: list[int]) -> None:
    tmp: list[int] = []
    tmp.append(find_number_above_center(grid, y, x))
    tmp.append(find_number_above_right(grid, y, x))
    tmp.append(find_number_above_left(grid, y, x))
    tmp.append(find_number_right(grid, y, x))
    tmp.append(find_number_left(grid, y, x))
    tmp.append(find_number_below_center(grid, y, x))
    tmp.append(find_number_below_right(grid, y, x))
    tmp.append(find_number_below_left(grid, y, x))
    numbers: list[int] = list(filter(lambda a: a != -1, tmp))
    if len(numbers) == 2:
        ratios.append(numbers[0] * numbers[1])
    return

def calculate_result_part_2(grid: list[str]) -> int :
    ratios: list[int] = []
    for y, row in enumerate(grid):
        for x in range(0, len(row)):
            if is_gear(grid[y][x]):
                save_gear_ratio(grid, y, x, ratios)
            else:
                x += 1
    return sum(ratios)

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

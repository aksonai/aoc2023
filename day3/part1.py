# --- Day 3: Gear Ratios ---
#
# You and the Elf eventually reach a gondola lift station; he says the gondola
# lift will take you up to the water source, but this is as far as he can
# bring you. You go inside.
#
# It doesn't take long to find the gondolas, but there seems to be a problem:
# they're not moving.
#
# "Aaah!"
#
# You turn around to see a slightly-greasy Elf with a wrench and a look of
# surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working
# right now; it'll still be a while before I can fix it." You offer to help.
#
# The engineer explains that an engine part seems to be missing from the
# engine, but nobody can figure out which one. If you can add up all the part
# numbers in the engine schematic, it should be easy to work out which part is
# missing.
#
# The engine schematic (your puzzle input) consists of a visual representation
# of the engine. There are lots of numbers and symbols you don't really
# understand, but apparently any number adjacent to a symbol, even diagonally,
# is a "part number" and should be included in your sum. (Periods (.) do not
# count as a symbol.)
#
# Here is an example engine schematic:
#
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
#
# In this schematic, two numbers are not part numbers because they are not
# adjacent to a symbol: 114 (top right) and 58 (middle right). Every other
# number is adjacent to a symbol and so is a part number; their sum is 4361.
#
# Of course, the actual engine schematic is much larger. What is the sum of
# all of the part numbers in the engine schematic?


f = open('input.txt', 'r')
LINES = f.readlines()


def get_symbol_coordinates() -> list[tuple[int, int]]:
    coordinates = []
    for i, line in enumerate(LINES):
        for j, char in enumerate(line.strip()):
            if not char.isdigit() and not char == '.':
                coordinates.append((i, j))
    return coordinates


SYMBOL_COORDINATES = get_symbol_coordinates()


def get_symbol_coverage_area() -> list[tuple[int, int]]:
    coverage_area = []
    for i, j in SYMBOL_COORDINATES:
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                coverage_area.append((x, y))
    return coverage_area


COVERAGE_AREA = get_symbol_coverage_area()


def process_line(line: str, line_number: int) -> int:
    parts_sum = 0
    current_number = ''
    add_number = False
    for i, ch in enumerate(line):
        if ch.isdigit():
            current_number += ch
            if (line_number, i) in COVERAGE_AREA:
                add_number = True
        else:
            if add_number:
                parts_sum += int(current_number)
                add_number = False
            current_number = ''
    return parts_sum


all_parts_sum = 0
for i, line in enumerate(LINES):
    all_parts_sum += process_line(line, i)

print(all_parts_sum)

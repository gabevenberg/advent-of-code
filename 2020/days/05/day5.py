#! /usr/bin/env python3

import pathlib
import sys
import re
from dataclasses import dataclass
from pprint import pprint

def row_to_int(string: str)->int:
    return int(string.replace('F','0').replace('B','1'),2)

def col_to_int(string: str)->int:
    return int(string.replace('L','0').replace('R','1'),2)

def parse(puzzle_input: str):
    """Parse input"""
    rows_and_cols = [(row_to_int(x[:7]),col_to_int(x[7:])) for x in puzzle_input.splitlines()]
    return set([x[0]*8+x[1] for x in rows_and_cols])

def part1(data):
    """Solve part 1"""
    return max(data)

def part2(data):
    """Solve part 2"""
    for row in range(128):
        for col in range(8):
            potentialID=row*8+col
            if potentialID not in data:
                if (potentialID+1 in data) and (potentialID-1 in data):
                    return potentialID

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

#! /usr/bin/env python3

import pathlib
import sys
import re
from dataclasses import dataclass
from pprint import pprint

def parse(puzzle_input: str):
    """Parse input"""
    # returns a 2 dimentional array where true means there is a tree there.
    return [[i=='#' for i in j] for j in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1"""
    return solveForSlope(data, 3, 1)

def solveForSlope(data, right: int, down: int):
    return sum(1 for index, row in enumerate(data[::down]) if row[(right*index)%len(row)])

def part2(data):
    """Solve part 2"""
    return solveForSlope(data,1,1)*solveForSlope(data,3,1)*solveForSlope(data,5,1)*solveForSlope(data,7,1)*solveForSlope(data,1,2)

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

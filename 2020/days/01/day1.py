#! /usr/bin/env python3

import pathlib
import sys
import re
from dataclasses import dataclass

def parse(puzzle_input):
    """Parse input"""
    return [int(string) for string in puzzle_input.splitlines()]

def part1(data:list[int]):
    """Solve part 1"""
    data.sort()
    while True:
        if len(data)<2:
            raise ValueError('no match found')
        s = data[0]+data[-1]
        if s>2020:
            data.pop(-1)
        elif s<2020:
            data.pop(0)
        else:
            return data[0]*data[-1]

def part2(data):
    """Solve part 2"""
    data.sort()
    while True:
        if len(data)<3:
            raise ValueError('no match found')
        if data[0]+data[1]+data[-1]>2020:
            data.pop(-1)
        elif data[0]+data[-1]+data[-2]<2020:
            data.pop(0)
        elif data[0]+data[1]+data[-1]==2020:
            return data[0]*data[1]*data[-1]
        else:
            return data[0]*data[-1]*data[-2]

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data.copy())
    solution2 = part2(data.copy())

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

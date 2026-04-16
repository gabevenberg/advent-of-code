#! /usr/bin/env python3

import pathlib
import sys
import re
from dataclasses import dataclass
from pprint import pprint

def parse(puzzle_input: str):
    """Parse input"""
    records = [[list(y) for y in x.splitlines()] for x in puzzle_input.split('\n\n')]
    return records

def part1(data):
    """Solve part 1"""
    results = []
    for group in data:
        result = set()
        for person in group:
            result |= set(person)
        results.append(len(result))
    return sum(results)

def part2(data):
    """Solve part 2"""
    results = []
    for group in data:
        result = set(group[0])
        for person in group:
            result &= set(person)
        results.append(len(result))
    return sum(results)

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

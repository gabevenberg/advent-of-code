#! /usr/bin/env python3

import pathlib
import sys
import re
from dataclasses import dataclass

@dataclass
class PasswordSpec:
    first:int
    second:int
    letter:str
    password:str

def parse(puzzle_input: str):
    """Parse input"""
    regex = re.compile(r'^(\d+)-(\d+) (\w): (\w+)$')
    toInt = lambda x: PasswordSpec(int(x[0]), int(x[1]), x[2], x[3])
    return [toInt(regex.match(i).groups()) for i in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1"""
    test = lambda x: x.first<=x.password.count(x.letter)<=x.second
    # these two lines are equivilant.
    # return sum(1 for p in data if test(p))
    return len([1 for p in data if test(p)])

def test_password(passwordSpec: PasswordSpec):
    if passwordSpec.password[passwordSpec.first-1]==passwordSpec.letter:
        return passwordSpec.password[passwordSpec.second-1]!=passwordSpec.letter
    else:
        return passwordSpec.password[passwordSpec.second-1]==passwordSpec.letter

def part2(data):
    """Solve part 2"""
    return sum(1 for p in data if test_password(p))

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

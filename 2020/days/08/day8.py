#! /usr/bin/env python3

from enum import StrEnum, auto
from dataclasses import dataclass
import pathlib
import sys


class OpCode(StrEnum):
    ACC = auto()
    JMP = auto()
    NOP = auto()


@dataclass
class Instruction:
    opcode: OpCode
    argument: int
    visited: bool = False


class VM:
    program: list[Instruction]
    acc: int
    program_counter: int

    def __init__(self, program: list[Instruction]) -> None:
        self.program = program
        self.reset()

    def reset(self):
        for instruction in self.program:
            instruction.visited = False
        self.acc = 0
        self.program_counter = 0

    def step(self) -> bool:
        """Returns the value of the acc and whether the program can continue"""
        match self.program[self.program_counter]:
            case Instruction(visited=True):
                return False
            case Instruction(opcode=OpCode.ACC, argument=arg):
                self.program[self.program_counter].visited = True
                self.acc += arg
                self.program_counter += 1
                return True
            case Instruction(opcode=OpCode.JMP, argument=arg):
                self.program[self.program_counter].visited = True
                self.program_counter += arg
                return True
            case Instruction(opcode=OpCode.NOP):
                self.program[self.program_counter].visited = True
                self.program_counter += 1
                return True
            case _:
                raise ValueError

    def run(self) -> tuple[int, int]:
        while self.step():
            pass
        return (self.acc, self.program_counter)


def parse(puzzle_input: str) -> list[Instruction]:
    """Parse input"""
    return [parse_line(line) for line in puzzle_input.splitlines()]


def parse_line(line: str) -> Instruction:
    opcodestr, argstr = line.split()
    return Instruction(OpCode(opcodestr), int(argstr))


def part1(program: list[Instruction]):
    """Solve part 1"""
    return VM(program).run()[0]


def part2(data):
    """Solve part 2"""


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

#! /usr/bin/env python3

import pathlib
import pytest
import day8 as aoc
from day8 import Instruction, OpCode

PUZZLE_DIR = pathlib.Path(__file__).parent

#these test fixtures setup the test, mainly by reading the filename into a string in this simple case.
@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [
            Instruction(OpCode.NOP, 0),
            Instruction(OpCode.ACC, 1),
            Instruction(OpCode.JMP, 4),
            Instruction(OpCode.ACC, 3),
            Instruction(OpCode.JMP, -3),
            Instruction(OpCode.ACC, -99),
            Instruction(OpCode.ACC, 1),
            Instruction(OpCode.JMP, -4),
            Instruction(OpCode.ACC, 6),
            ]

def test_part1_example(example):
    """Test part 1 on example input"""
    assert aoc.part1(example) == 5

@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input"""
    assert aoc.part2(example) == ...

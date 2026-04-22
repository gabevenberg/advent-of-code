#! /usr/bin/env python3

import pathlib
import pytest
import day5 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


# these test fixtures setup the test, mainly by reading the filename into a string in this simple case.
@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse(example):
    """Test that input is parsed properly"""
    assert example == {119, 357, 567, 820}


def test_part1(example):
    """Test part 1 on example input"""
    assert aoc.part1(example) == 820


def test_part2(example):
    """Test part 2 on example input"""
    assert aoc.part2(example) is None

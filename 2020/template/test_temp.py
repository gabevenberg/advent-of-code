#! /usr/bin/env python3

import pathlib
import pytest
import temp as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

#these test fixtures setup the test, mainly by reading the filename into a string in this simple case.
@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.mark.skip(reason="Not implemented")
def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == ...

@pytest.mark.skip(reason="Not implemented")
def test_part1_example(example):
    """Test part 1 on example input"""
    assert aoc.part1(example) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input"""
    assert aoc.part2(example) == ...

#! /usr/bin/env python3

import pathlib
import pytest
import day2 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

#these test fixtures setup the test, mainly by reading the filename into a string in this simple case.
@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2").read_text().strip()
    return aoc.parse(puzzle_input)

# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
            aoc.PasswordSpec(first=1, second=3, letter='a', password='abcde'),
            aoc.PasswordSpec(first=1, second=3, letter='b', password='cdefg'),
            aoc.PasswordSpec(first=2, second=9, letter='c', password='ccccccccc')
            ]

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 2

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 1

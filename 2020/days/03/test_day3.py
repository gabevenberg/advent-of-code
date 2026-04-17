#! /usr/bin/env python3

import pathlib
import pytest
import day3 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


# these test fixtures setup the test, mainly by reading the filename into a string in this simple case.
@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse(example):
    """Test that input is parsed properly"""
    assert example == [
        [False, False, True, True, False, False, False, False, False, False, False],
        [True, False, False, False, True, False, False, False, True, False, False],
        [False, True, False, False, False, False, True, False, False, True, False],
        [False, False, True, False, True, False, False, False, True, False, True],
        [False, True, False, False, False, True, True, False, False, True, False],
        [False, False, True, False, True, True, False, False, False, False, False],
        [False, True, False, True, False, True, False, False, False, False, True],
        [False, True, False, False, False, False, False, False, False, False, True],
        [True, False, True, True, False, False, False, True, False, False, False],
        [True, False, False, False, True, True, False, False, False, False, True],
        [False, True, False, False, True, False, False, False, True, False, True],
    ]


# @pytest.mark.skip(reason="Not implemented")
def test_part1(example):
    """Test part 1 on example input"""
    assert aoc.part1(example) == 7


# @pytest.mark.skip(reason="Not implemented")
def test_part2(example):
    """Test part 2 on example input"""
    assert aoc.part2(example) == 336

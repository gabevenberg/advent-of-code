#! /usr/bin/env python3

import pathlib
import pytest
import day7 as aoc
from day7 import Bag

PUZZLE_DIR = pathlib.Path(__file__).parent


# these test fixtures setup the test, mainly by reading the filename into a string in this simple case.
@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse(example):
    """Test that input is parsed properly"""
    assert example == {
        Bag("light", "red"): {
            Bag("bright", "white"): 1,
            Bag("muted", "yellow"): 2,
        },
        Bag("dark", "orange"): {
            Bag("bright", "white"): 3,
            Bag("muted", "yellow"): 4,
        },
        Bag("bright", "white"): {Bag("shiny", "gold"): 1},
        Bag("muted", "yellow"): {
            Bag("shiny", "gold"): 2,
            Bag("faded", "blue"): 9,
        },
        Bag("shiny", "gold"): {
            Bag("dark", "olive"): 1,
            Bag("vibrant", "plum"): 2,
        },
        Bag("dark", "olive"): {
            Bag("faded", "blue"): 3,
            Bag("dotted", "black"): 4,
        },
        Bag("vibrant", "plum"): {
            Bag("faded", "blue"): 5,
            Bag("dotted", "black"): 6,
        },
        Bag("faded", "blue"): {},
        Bag("dotted", "black"): {},
    }


def test_find_direct_holders(example):
    assert aoc.find_direct_holders(Bag("shiny", "gold"), example) == set(
        [Bag("bright", "white"), Bag("muted", "yellow")]
    )


def test_part1(example):
    """Test part 1 on example input"""
    assert aoc.part1(example) == 4


@pytest.mark.skip(reason="Not implemented")
def test_part2(example):
    """Test part 2 on example input"""
    assert aoc.part2(example) == ...

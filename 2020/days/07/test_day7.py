#! /usr/bin/env python3

import pathlib
import pytest
import day7 as aoc
from day7 import Bag, Color, Descriptor

PUZZLE_DIR = pathlib.Path(__file__).parent


# these test fixtures setup the test, mainly by reading the filename into a string in this simple case.
@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse(example):
    """Test that input is parsed properly"""
    assert example == {
        Bag(Descriptor.LIGHT, Color.RED): {
            Bag(Descriptor.BRIGHT, Color.WHITE): 1,
            Bag(Descriptor.MUTED, Color.YELLOW): 2,
        },
        Bag(Descriptor.DARK, Color.ORANGE): {
            Bag(Descriptor.BRIGHT, Color.WHITE): 3,
            Bag(Descriptor.MUTED, Color.YELLOW): 4,
        },
        Bag(Descriptor.BRIGHT, Color.WHITE): {Bag(Descriptor.SHINY, Color.GOLD): 1},
        Bag(Descriptor.MUTED, Color.YELLOW): {
            Bag(Descriptor.SHINY, Color.GOLD): 2,
            Bag(Descriptor.FADED, Color.BLUE): 9,
        },
        Bag(Descriptor.SHINY, Color.GOLD): {
            Bag(Descriptor.DARK, Color.OLIVE): 1,
            Bag(Descriptor.VIBRANT, Color.PLUM): 2,
        },
        Bag(Descriptor.DARK, Color.OLIVE): {
            Bag(Descriptor.FADED, Color.BLUE): 3,
            Bag(Descriptor.DOTTED, Color.BLACK): 4,
        },
        Bag(Descriptor.VIBRANT, Color.PLUM): {
            Bag(Descriptor.FADED, Color.BLUE): 5,
            Bag(Descriptor.DOTTED, Color.BLACK): 6,
        },
        Bag(Descriptor.FADED, Color.BLUE): {},
        Bag(Descriptor.DOTTED, Color.BLACK): {},
    }


@pytest.mark.skip(reason="Not implemented")
def test_part1(example):
    """Test part 1 on example input"""
    assert aoc.part1(example) == 4


@pytest.mark.skip(reason="Not implemented")
def test_part2(example):
    """Test part 2 on example input"""
    assert aoc.part2(example) == ...

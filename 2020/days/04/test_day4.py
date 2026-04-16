#! /usr/bin/env python3

import pathlib
import pytest
import day4 as aoc
from day4 import Passport

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
    assert example1 == [Passport(birthYear=1937,
        issueYear=2017,
        expirationYear=2020,
        height='183cm',
        hairColor='#fffffd',
        eyeColor='gry',
        passportId='860033327',
        countryId='147'),
        Passport(birthYear=1929,
            issueYear=2013,
            expirationYear=2023,
            height=None,
            hairColor='#cfa07d',
            eyeColor='amb',
            passportId='028048884',
            countryId='350'),
        Passport(birthYear=1931,
            issueYear=2013,
            expirationYear=2024,
            height='179cm',
            hairColor='#ae17e1',
            eyeColor='brn',
            passportId='760753108',
            countryId=None),
        Passport(birthYear=None,
            issueYear=2011,
            expirationYear=2025,
            height='59in',
            hairColor='#cfa07d',
            eyeColor='brn',
            passportId='166559648',
            countryId=None)]

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 2

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 2

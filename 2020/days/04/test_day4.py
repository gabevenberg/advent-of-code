#! /usr/bin/env python3

import pathlib
import pytest
import day4 as aoc
from day4 import Passport

PUZZLE_DIR = pathlib.Path(__file__).parent


# these test fixtures setup the test, mainly by reading the filename into a string in this simple case.
@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse(example):
    """Test that input is parsed properly"""
    assert example == [
        Passport(
            birthYear=1937,
            issueYear=2017,
            expirationYear=2020,
            height="183cm",
            hairColor="#fffffd",
            eyeColor="gry",
            passportId="860033327",
            countryId="147",
        ),
        Passport(
            birthYear=1929,
            issueYear=2013,
            expirationYear=2023,
            height=None,
            hairColor="#cfa07d",
            eyeColor="amb",
            passportId="028048884",
            countryId="350",
        ),
        Passport(
            birthYear=1931,
            issueYear=2013,
            expirationYear=2024,
            height="179cm",
            hairColor="#ae17e1",
            eyeColor="brn",
            passportId="760753108",
            countryId=None,
        ),
        Passport(
            birthYear=None,
            issueYear=2011,
            expirationYear=2025,
            height="59in",
            hairColor="#cfa07d",
            eyeColor="brn",
            passportId="166559648",
            countryId=None,
        ),
    ]


# @pytest.mark.skip(reason="Not implemented")
def test_part1(example):
    """Test part 1 on example input"""
    assert aoc.part1(example) == 2


# @pytest.mark.skip(reason="Not implemented")
def test_part2(example):
    """Test part 2 on example input"""
    assert aoc.part2(example) == 2

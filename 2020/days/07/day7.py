#! /usr/bin/env python3

import sys
from typing import Dict
from dataclasses import dataclass
from enum import StrEnum, auto
import pathlib

import parsy


class Color(StrEnum):
    RED = auto()
    ORANGE = auto()
    WHITE = auto()
    YELLOW = auto()
    GOLD = auto()
    OLIVE = auto()
    PLUM = auto()
    BLUE = auto()
    BLACK = auto()


class Descriptor(StrEnum):
    LIGHT = auto()
    DARK = auto()
    BRIGHT = auto()
    MUTED = auto()
    SHINY = auto()
    VIBRANT = auto()
    FADED = auto()
    DOTTED = auto()


@dataclass(frozen=True)
class Bag:
    descriptor: Descriptor
    color: Color


def parse(puzzle_input: str) -> dict[Bag, dict[Bag, int]]:
    """Parse input"""
    ret = {}
    for line in puzzle_input.splitlines():
        bag, rule = parse_line(line)
        ret[bag] = rule
    return ret


def parse_line(input: str) -> tuple[Bag, dict[Bag, int]]:
    bagstr, _, rulesstr = input.partition(" contain ")
    d, c = parse_bag().parse(bagstr.strip())
    bag = Bag(d, c)
    rules = parse_rules().parse(rulesstr.strip())
    print(bag, rules)
    rules = {Bag(r[1][0], r[1][1]): r[0] for r in rules}
    return (bag, rules)


def parse_rules() -> parsy.Parser:
    return parsy.alt(
        parse_rule().at_least(1),
        parsy.string_from("no other bags.").map(lambda _: []),
    )


def parse_rule() -> parsy.Parser:
    return parsy.seq(
        parsy.regex("[0-9]+").map(int) << parsy.whitespace,
        parse_bag() << parsy.string_from(", ", "."),
    )


def parse_bag() -> parsy.Parser:
    descriptorparser = parsy.from_enum(Descriptor).desc("descriptor")
    colorparser = parsy.from_enum(Color).desc("color")
    return parsy.seq(
        descriptorparser << parsy.whitespace,
        colorparser << parsy.whitespace << parsy.string_from("bag", "bags"),
    )


def part1(data):
    """Solve part 1"""


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

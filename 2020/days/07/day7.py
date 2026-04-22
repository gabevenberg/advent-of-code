#! /usr/bin/env python3

import sys
from dataclasses import dataclass
import pathlib

import parsy


@dataclass(frozen=True)
class Bag:
    descriptor: str
    color: str


type Rules = dict[Bag, dict[Bag, int]]


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
    descriptorparser = parsy.regex(r"\w+").desc("descriptor")
    colorparser = parsy.regex(r"\w+").desc("color")
    return parsy.seq(
        descriptorparser << parsy.whitespace,
        colorparser << parsy.whitespace << parsy.string_from("bag", "bags"),
    )


def find_direct_holders(bag: Bag, rules: Rules) -> set[Bag]:
    ret = set()
    for container, contents in rules.items():
        for content in contents.keys():
            if content == bag:
                ret.add(container)
    return ret


def part1(rules: Rules):
    """Solve part 1"""
    solution = set()
    search = set([Bag("shiny", "gold")])
    while len(search) != 0:
        bags = find_direct_holders(search.pop(), rules)
        for bag in bags:
            solution.add(bag)
            search.add(bag)
    return len(solution)


def find_nested_bags(bag: Bag, rules: Rules) -> int:
    if rules[bag] == {}:
        return 0
    else:
        return sum([i + (find_nested_bags(b, rules) * i) for b, i in rules[bag].items()])


def part2(rules):
    """Solve part 2"""
    return find_nested_bags(Bag("shiny", "gold"), rules)


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

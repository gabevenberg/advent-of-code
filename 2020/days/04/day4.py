#! /usr/bin/env python3

import pathlib
import sys
import re
from dataclasses import dataclass
from pprint import pprint

@dataclass
class Passport:
    birthYear: int | None
    issueYear: int | None
    expirationYear: int | None
    height: str | None
    hairColor: str | None
    eyeColor: str | None
    passportId: str | None
    countryId: str | None

def regexUnwrap(match, group:int)->str | None:
    return match[group] if match is not None else None

def parse(puzzle_input: str)->list[Passport]:
    """Parse input"""
    rawRecords = [i.replace('\n', ' ') for i in puzzle_input.split('\n\n')]
    records = []
    for rawRecord in rawRecords:
        birthYear=re.search(r'byr:(\S+)', rawRecord)
        issueYear=re.search(r'iyr:(\S+)', rawRecord)
        expirationYear=re.search(r'eyr:(\S+)', rawRecord)
        height=re.search(r'hgt:(\S+)', rawRecord)
        hairColor=re.search(r'hcl:(\S+)', rawRecord)
        eyeColor=re.search(r'ecl:(\S+)', rawRecord)
        passportId=re.search(r'pid:(\S+)', rawRecord)
        countryId=re.search(r'cid:(\S+)', rawRecord)
        records.append(Passport(
            int(birthYear[1]) if birthYear is not None else None,
            int(issueYear[1]) if issueYear is not None else None,
            int(expirationYear[1]) if expirationYear is not None else None,
            regexUnwrap(height,1),
            regexUnwrap(hairColor,1),
            regexUnwrap(eyeColor,1),
            regexUnwrap(passportId,1),
            regexUnwrap(countryId,1),
        ))
    return records

def lazyCheckPassport(passport: Passport)->bool:
    return (
            passport.birthYear is not None
            and passport.issueYear is not None
            and passport.expirationYear is not None
            and passport.height is not None
            and passport.hairColor is not None
            and passport.eyeColor is not None
            and passport.passportId is not None
            )

def part1(data):
    """Solve part 1"""
    return sum(1 for record in data if lazyCheckPassport(record))

def checkBirthYear(passport: Passport)->bool:
    if passport.birthYear is None: return False
    return (1920<=passport.birthYear<=2002)

def checkIssueYear(passport: Passport)->bool:
    if passport.issueYear is None: return False
    return (2010<=passport.issueYear<=2020)

def checkExpirationYear(passport: Passport)->bool:
    if passport.expirationYear is None: return False
    return (2020<=passport.expirationYear<=2030)

def checkHeight(passport: Passport)->bool:
    if passport.height is None: return False
    rematch = re.match(r'(\d+)((?:in)|(?:cm))', passport.height)
    if rematch is None: return False
    number = int(rematch.group(1))
    unit = rematch.group(2)
    if unit == 'in':
        return (59<=number<=76)
    else:
        return (150<=number<=193)

def checkHairColour(passport: Passport)->bool:
    if passport.hairColor is None: return False
    return (re.match(r'#[0123456789abcdef]{6}$', passport.hairColor) is not None)

def checkEyeColour(passport: Passport)->bool:
    if passport.eyeColor is None: return False
    return (passport.eyeColor == 'amb'
            or passport.eyeColor == 'blu'
            or passport.eyeColor == 'brn'
            or passport.eyeColor == 'gry'
            or passport.eyeColor == 'grn'
            or passport.eyeColor == 'hzl'
            or passport.eyeColor == 'oth'
            )

def checkPassportId(passport: Passport)->bool:
    if passport.passportId is None: return False
    return (re.match(r'[0-9]{9}$', passport.passportId) is not None)

def checkPassport(passport: Passport)->bool:
    return (checkBirthYear(passport)
            and checkIssueYear(passport)
            and checkExpirationYear(passport)
            and checkHeight(passport)
            and checkHairColour(passport)
            and checkEyeColour(passport)
            and checkPassportId(passport)
            )

def part2(data):
    """Solve part 2"""
    return sum(1 for record in data if checkPassport(record))

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

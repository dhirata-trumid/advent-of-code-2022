from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcomes(Enum):
    WIN = 6
    TIE = 3
    LOSS = 0


class Match:
    def __init__(self, opp, you):
        self.opp = opp
        self.you = you

    def outcome_calculater(self):
        if self.opp.value == self.you.value:
            return Outcomes.TIE.value
        elif self.opp.value % 3 == (self.you.value + 1) % 3:
            return Outcomes.LOSS.value
        else:
            return Outcomes.WIN.value

    def calc_match_points(self):
        return self.you.value + self.outcome_calculater()


def outcome_to_play(outcome, opp):
    if outcome == Outcomes.TIE:
        return opp
    elif outcome == Outcomes.WIN:
        enum_val = opp.value + 1
        enum_val = enum_val if enum_val <= 3 else 1
        return RPS(enum_val)
    else:
        enum_val = opp.value - 1
        enum_val = enum_val if enum_val != 0 else 3
        return RPS(enum_val)


# TEXT PARSING
def mapper(i):
    if i == "A" or i == "X":
        return RPS.ROCK
    elif i == "B" or i == "Y":
        return RPS.PAPER
    else:
        return RPS.SCISSORS


def map_row_to_rps(row):
    inputs = row.split()
    return map(mapper, inputs)


def map_row_to_input_outcome(row):
    opp, out = row.split()
    if out == "X":
        outcome = Outcomes.LOSS
    elif out == "Y":
        outcome = Outcomes.TIE
    else:
        outcome = Outcomes.WIN
    return [mapper(opp), outcome]


# RUNNERS
def part_1():
    total = 0
    with open("sample/rps_input.txt") as f:
        lines = map(map_row_to_rps, f.readlines())
    for line in lines:
        match = list(line)
        total += Match(match[0], match[1]).calc_match_points()
    return total


def part_2():
    total = 0
    with open("sample/rps_input.txt") as f:
        lines = map(map_row_to_input_outcome, f.readlines())
    for line in lines:
        match = list(line)
        total += Match(
            match[0], outcome_to_play(match[1], match[0])
        ).calc_match_points()
    return total


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

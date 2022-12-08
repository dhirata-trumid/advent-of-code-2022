import re


def setup_stacks(num_stacks=9):
    return [[] for i in range(num_stacks)]


def init_stacks(lines, spacing=4):
    stacks = setup_stacks()
    setup_lines = lines[0:8]
    for line in setup_lines:
        stack_i = 0
        for i in range(1, len(line), 4):
            c = line[i]
            if c != " ":
                stacks[stack_i].insert(0, c)
            stack_i += 1
    return stacks


def move_stacks_9k(lines, stacks):
    instructions = lines[10:]
    for line in instructions:
        line = line.replace(" ", "").strip()
        line = line.replace("move", "").replace("from", ",").replace("to", ",")
        count, source, dest = line.split(",")
        for i in range(int(count)):
            crate = stacks[int(source) - 1].pop()
            stacks[int(dest) - 1].append(crate)
    return stacks


def part_1():
    with open("sample/supplystacks.txt") as f:
        lines = f.readlines()
    stacks = init_stacks(lines)
    # print(stacks)
    stacks = move_stacks_9k(lines, stacks)
    return "".join([stack.pop() for stack in stacks])


def move_stacks_9k1(lines, stacks):
    instructions = lines[10:]
    for line in instructions:
        line = line.replace(" ", "").strip()
        line = line.replace("move", "").replace("from", ",").replace("to", ",")
        count, source, dest = line.split(",")

        crates = stacks[int(source) - 1][-int(count) :]
        stacks[int(source) - 1] = stacks[int(source) - 1][: -int(count)]
        stacks[int(dest) - 1].extend(crates)
    return stacks


def part_2():
    with open("sample/supplystacks.txt") as f:
        lines = f.readlines()
    stacks = init_stacks(lines)
    # print(stacks)
    stacks = move_stacks_9k1(lines, stacks)
    return "".join([stack.pop() for stack in stacks])


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

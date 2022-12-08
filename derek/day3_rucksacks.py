import string


def get_ascii_value_map():
    res = {}
    all_letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    for i, letter in enumerate(all_letters):
        res[letter] = i + 1
    return res


def open_rucksack(path="sample/rucksack.txt"):
    lines = []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            line_size = len(line)
            lines.append([line[: line_size // 2], line[line_size // 2 :]])
    return lines


def get_compartment_similarities(rucksack):
    result = []
    for c1, c2 in rucksack:
        # rm dupes
        c1 = "".join(set(c1))
        for item in c1:
            if item in c2:
                result.append(item)
    return result


def part_1():
    priority_map = get_ascii_value_map()
    rucksack = open_rucksack()
    similarities = get_compartment_similarities(rucksack)
    return sum([*map(priority_map.get, similarities)])


def get_group_badges(rucksack, n=3):
    result = []
    rucksack = [c1 + c2 for c1, c2 in rucksack]
    elf_groups = [rucksack[i : i + n] for i in range(0, len(rucksack), n)]
    for e1, e2, e3 in elf_groups:
        e1 = set(e1)
        e2 = set(e2)
        e3 = set(e3)
        if e1 & e2 & e3:
            result.extend(e1 & e2 & e3)
    return result


def part_2():
    priority_map = get_ascii_value_map()
    rucksack = open_rucksack()
    badges = get_group_badges(rucksack)
    return sum([*map(priority_map.get, badges)])


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

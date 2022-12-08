def open_cleanup_schedule(path="sample/camp_cleanup.txt"):
    lines = []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            shift1, shift2 = line.split(",")
            s1 = shift1.split("-")
            enum_shift1 = set(range(int(s1[0]), int(s1[-1]) + 1))
            s2 = shift2.split("-")
            enum_shift2 = set(range(int(s2[0]), int(s2[-1]) + 1))
            lines.append([enum_shift1, enum_shift2])
    return lines


def find_overlap(schedule, func):
    result = 0
    for s1, s2 in schedule:
        if func(s1, s2):
            result += 1
    return result


def part_1():
    schedule = open_cleanup_schedule()
    return find_overlap(schedule, lambda x, y: x.issuperset(y) or y.issuperset(x))


def part_2():
    schedule = open_cleanup_schedule()
    return find_overlap(schedule, lambda x, y: x.intersection(y))


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

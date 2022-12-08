def read_input(path="sample/calorie_input.txt"):
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]
    chunk = []
    for value in lines:
        if not value:
            yield sum(chunk)
            chunk = []
        else:
            chunk.append(int(value))
    yield sum(chunk)


def part_1():
    biggest_cal = 0
    for curr_cal in read_input():
        biggest_cal = max(curr_cal, biggest_cal)
    return biggest_cal


def part_2():
    return sum(sorted(read_input())[-3:])


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

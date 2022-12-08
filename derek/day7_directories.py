from __future__ import annotations

from typing import Union


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    @classmethod
    def add_child(cls, d: Dir, child: Union[File, Dir]):
        for c in d.children:
            # should guarentee idempotence?
            if c.name == child.name:
                return False
        d.children.append(child)
        if isinstance(child, File):
            file_size = child.size
            d.size += file_size

            current = d.parent
            while current is not None:
                current.size += file_size
                current = current.parent
        return True


def parse_input(path="sample/directory_nav.txt"):
    dirs = []
    with open(path) as f:
        lines = f.readlines()
    root = Dir("/", None)
    dirs.append(root)
    current = root
    for line in lines:
        line = line.split()
        if line[0] == "$":
            # it's a command either cd or ls
            if line[1] == "cd":
                dest_name = line[2]
                if dest_name == "/":
                    current = root
                elif dest_name == "..":
                    current = current.parent
                else:
                    dest = Dir(dest_name, current)
                    if Dir.add_child(current, dest):
                        dirs.append(dest)
                    current = dest
            # I think I can ignore ls's
        elif line[0] != "dir":
            f = File(line[1], int(line[0]))
            Dir.add_child(current, f)
    return dirs


def part_1():
    all_dirs = parse_input()
    total = 0
    for d in all_dirs:
        if d.size <= 100000:
            total += d.size
    print(total)


def part_2():
    all_dirs = parse_input()
    total = 70000000
    req = 30000000
    used = all_dirs[0].size  # root
    some_dir_sizes = []
    for d in all_dirs:
        if d.size >= (req - (total - used)):
            some_dir_sizes.append(d.size)
    print(sorted(some_dir_sizes)[0])


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()

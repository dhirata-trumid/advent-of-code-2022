def parse_input(path="sample/tree.txt"):
    with open(path) as f:
        tree_matrix = [list(map(int, list(l.strip()))) for l in f.readlines()]
    return tree_matrix


def get_vis_matrix(tree_matrix):
    return [[0] * len(tree_matrix[0]) for _ in range(len(tree_matrix))]


def check_visibility_row(i, l):
    if i == 0 or i == (len(l) - 1):
        return True
    val = l[i]
    if (max(l[:i]) < val) or (max(l[i + 1 :]) < val):
        return True
    else:
        return False


def column(matrix, i):
    return [row[i] for row in matrix]


def traverse_matrix(tree_matrix, func):
    vis_matrix = get_vis_matrix(tree_matrix)
    for i in range(len(tree_matrix)):
        for j in range(len(tree_matrix[0])):
            vis_matrix[i][j] = func(i, j, tree_matrix)
    return vis_matrix


def part_1():
    tree_matrix = parse_input()
    vis_matrix = traverse_matrix(
        tree_matrix,
        lambda i, j, m: 1
        if check_visibility_row(j, m[i]) or check_visibility_row(i, column(m, j))
        else 0,
    )
    return sum(map(sum, vis_matrix))


def helper(val, row):
    result = 0
    for i in row:
        result += 1
        if val <= i:
            break
    return result


def calc_scenic_score_row(i, row):
    if i == 0 or i == (len(row) - 1):
        return 0
    val = row[i]
    return helper(val, row[:i][::-1]) * helper(val, row[i + 1 :])


def part_2():
    tree_matrix = parse_input()
    score_matrix = traverse_matrix(
        tree_matrix,
        lambda i, j, m: calc_scenic_score_row(j, m[i])
        * calc_scenic_score_row(i, column(m, j)),
    )
    return max(map(max, score_matrix))


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

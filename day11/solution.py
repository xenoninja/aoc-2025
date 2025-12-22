from utils.read import read_file_by_line
from functools import cache


def solve_puzzle_one(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    moves_dict = dict()
    paths = list()

    for line in lines:
        i = line.split(":")[0]
        o = line.split(":")[1].split()
        moves_dict[i] = o

    traverse(moves_dict, paths, "you")

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #1's answer:", len(paths))
    print("=" * 10)


def traverse(moves_dict, paths, cur_node):
    if cur_node == "out":
        paths.append("done")
    elif cur_node not in moves_dict:
        return
    else:
        for i in moves_dict[cur_node]:
            traverse(moves_dict, paths, i)


def solve_puzzle_two(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    moves_dict = dict()
    res = 0

    for line in lines:
        i = line.split(":")[0]
        o = line.split(":")[1].split()
        moves_dict[i] = o

    @cache
    def count(start, target):
        if start == target:
            return 1
        elif start not in moves_dict:
            return 0
        else:
            return sum(count(i, target) for i in moves_dict[start])

    res += count("svr", "dac") * count("dac", "fft") * count("fft", "out")
    res += count("svr", "fft") * count("fft", "dac") * count("dac", "out")

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #2's answer:", res)
    print("=" * 10)


if __name__ == "__main__":
    solve_puzzle_one("./input/test")
    solve_puzzle_two("./input/another_test")

    solve_puzzle_one("./input/input")
    solve_puzzle_two("./input/input")

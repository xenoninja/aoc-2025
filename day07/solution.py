from collections import Counter
from utils.read import read_file_by_line, raw_read_file_by_line


def solve_puzzle_one(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    counts = 0

    beam_cols = set()
    start_row = 0
    start_col = 0

    for start_row in range(len(lines)):
        start_col = lines[start_row].find("S")
        if start_col != -1:
            break

    beam_cols.add(start_col)

    for cur_row in range(start_row, len(lines)):
        tmp_cols = list(beam_cols)
        for col in tmp_cols:
            if lines[cur_row][col] == "^":
                beam_cols.remove(col)
                beam_cols.add(col - 1)
                beam_cols.add(col + 1)
                counts += 1

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #1's answer:", counts)
    print("=" * 10)


def solve_puzzle_two(input_file):
    lines = raw_read_file_by_line(input_file)

    if lines is None:
        return

    start_row = 0
    start_col = 0
    paths = Counter()

    for start_row in range(len(lines)):
        start_col = lines[start_row].find("S")
        if start_col != -1:
            paths[start_col] = 1
            break

    for cur_row in range(start_row, len(lines)):
        for i in range(len(lines[cur_row])):
            if i in paths and lines[cur_row][i] == "^":
                paths[i - 1] += paths[i]
                paths[i + 1] += paths[i]
                del paths[i]

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #2's answer:", paths.total())
    print("=" * 10)


if __name__ == "__main__":
    # solve_puzzle_one("./input/test")
    solve_puzzle_two("./input/test")

    # solve_puzzle_one("./input/input")
    solve_puzzle_two("./input/input")

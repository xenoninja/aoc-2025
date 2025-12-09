from utils.read import read_file_by_line


def solve_puzzle_one(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    counts = 0

    grid_dict = dict()
    candidates = []

    rows = len(lines)
    cols = len(lines[0])

    for row in range(rows):
        for col in range(cols):
            grid_dict[(row, col)] = lines[row][col]
            if lines[row][col] == "@":
                candidates.append((row, col))

    for row, col in candidates:
        if is_acessable(grid_dict, row, col):
            counts += 1

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #1's answer:", counts)
    print("=" * 10)


def solve_puzzle_two(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    counts = 0

    grid_dict = dict()

    rows = len(lines)
    cols = len(lines[0])

    for row in range(rows):
        for col in range(cols):
            grid_dict[(row, col)] = lines[row][col]

    while True:
        candidates = []
        found = []

        for row in range(rows):
            for col in range(cols):
                if grid_dict[(row, col)] == "@":
                    candidates.append((row, col))

        for row, col in candidates:
            if is_acessable(grid_dict, row, col):
                counts += 1
                found.append((row, col))

        for row, col in found:
            grid_dict[(row, col)] = "."

        if len(found) == 0:
            break

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #2's answer:", counts)
    print("=" * 10)


def is_acessable(grid_dict, cur_row, cur_col):
    count = 0

    for row in range(cur_row - 1, cur_row + 2):
        for col in range(cur_col - 1, cur_col + 2):
            if (
                (row, col) in grid_dict
                and not (row == cur_row and col == cur_col)
                and grid_dict[(row, col)] == "@"
            ):
                count += 1

    return count < 4


if __name__ == "__main__":
    solve_puzzle_one("./input/test")
    solve_puzzle_two("./input/test")

    solve_puzzle_one("./input/input")
    solve_puzzle_two("./input/input")

from utils.read import read_file_by_line


def solve_puzzle_one(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    counts = 0
    ranges = []
    candidates = []

    for line in lines:
        if line == "":
            continue
        if "-" in line:
            tmp = line.split("-")
            ranges.append([int(i) for i in tmp])
        else:
            candidates.append(int(line))

    for candidate in candidates:
        for [a, b] in ranges:
            if a <= candidate <= b:
                counts += 1
                break

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #1's answer:", counts)
    print("=" * 10)


def solve_puzzle_two(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    counts = 0

    ranges = []

    for line in lines:
        if line == "":
            continue
        if "-" in line:
            tmp = line.split("-")
            ranges.append([int(i) for i in tmp])

    while True:
        merged_ranges = []
        for [a, b] in ranges:
            is_seperate = True
            for [c, d] in merged_ranges:
                if a > d or b < c:
                    continue
                else:
                    is_seperate = False
                    if c <= a and b <= d:
                        pass
                    elif c <= a and b > d:
                        merged_ranges.remove([c, d])
                        merged_ranges.append([c, b])
                    elif c > a and b <= d:
                        merged_ranges.remove([c, d])
                        merged_ranges.append([a, d])
                    elif a <= c and d <= b:
                        merged_ranges.remove([c, d])
                        merged_ranges.append([a, b])
                    break

            if is_seperate:
                merged_ranges.append([a, b])

        if len(ranges) == len(merged_ranges):
            break

        ranges = merged_ranges

    for [a, b] in merged_ranges:
        counts = counts + b - a + 1

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #2's answer:", counts)
    print("=" * 10)


if __name__ == "__main__":
    solve_puzzle_one("./input/test")
    solve_puzzle_two("./input/test")

    solve_puzzle_one("./input/input")
    solve_puzzle_two("./input/input")

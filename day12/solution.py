from utils.read import read_file_by_line


def solve_puzzle(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    candidates = list()
    candidate_sizes = list()
    res = 0

    for i in range(len(lines)):
        t = lines[i].split(":")[0]
        if "x" in t:
            size = int(t.split("x")[0]) * int(t.split("x")[1])
            nums = lines[i].split(":")[1].split()
            cnts = 0
            for j, num in enumerate(nums):
                cnts += int(num) * candidate_sizes[j]
            if cnts <= size:
                res += 1
        elif ":" in lines[i]:
            candidates.append([lines[i + 1], lines[i + 2], lines[i + 3]])
            candidate_sizes.append(
                lines[i + 1].count("#")
                + lines[i + 2].count("#")
                + lines[i + 3].count("#")
            )
            i += 4

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #1's answer:", res)
    print("=" * 10)


if __name__ == "__main__":
    # solve_puzzle("./input/test")

    solve_puzzle("./input/input")

from utils.read import read_file_by_line


def solve_puzzle(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    idx = 50
    fst_answer = 0
    snd_answer = 0

    for line in lines:
        dir = line[:1]
        dis = int(line[1:])

        for _ in range(dis):
            if dir == "L":
                idx -= 1
            else:
                idx += 1

            if idx == -1:
                idx = 99
            elif idx == 100:
                idx = 0
                snd_answer += 1
            elif idx == 0:
                snd_answer += 1

        if idx == 0:
            fst_answer += 1

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #1's answer:", fst_answer)
    print("Puzzle #2's answer:", snd_answer)
    print("=" * 10)


if __name__ == "__main__":
    solve_puzzle("./input/test")
    solve_puzzle("./input/another_test")
    solve_puzzle("./input/input")

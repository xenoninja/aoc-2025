from utils.read import read_file_by_line, raw_read_file_by_line


def solve_puzzle_one(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    counts = 0

    quantity = len(lines[0].split())
    candidates = [[] for _ in range(quantity)]

    for i in range(len(lines)):
        line = lines[i]

        if i < len(lines) - 1:
            num = line.split()
            for i in range(quantity):
                candidates[i].append(int(num[i]))
        else:
            calc_symbols = line.split()
            for i in range(quantity):
                match calc_symbols[i]:
                    case "+":
                        sum = 0
                        for num in candidates[i]:
                            sum += num
                        counts += sum
                    case "*":
                        sum = 1
                        for num in candidates[i]:
                            sum *= num
                        counts += sum
                    case _:
                        pass

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #1's answer:", counts)
    print("=" * 10)


def solve_puzzle_two(input_file):
    lines = raw_read_file_by_line(input_file)

    if lines is None:
        return

    counts = 0

    quantity = len(lines[-1].split())
    candidates = [[] for _ in range(quantity)]
    sym_idx = []

    sym_cnt = 0
    for i in range(len(lines[-1])):
        if lines[-1][i] != " ":
            sym_idx.append(i)
            sym_cnt += 1
    sym_idx.append(len(lines[-1]) + 1)

    num_cnts = len(lines) - 1

    for i in range(len(sym_idx) - 1):
        left_idx = sym_idx[i]
        right_idx = sym_idx[i + 1] - 2

        num_quantity = right_idx - left_idx + 1

        for j in range(num_quantity):
            num = ""
            for k in range(num_cnts - 1, -1, -1):
                num += lines[num_cnts - k - 1][left_idx + j]
            candidates[i].append(int(num))

    calc_symbols = lines[-1].split()
    for i in range(quantity):
        match calc_symbols[i]:
            case "+":
                sum = 0
                for num in candidates[i]:
                    sum += num
                counts += sum
            case "*":
                sum = 1
                for num in candidates[i]:
                    sum *= num
                counts += sum
            case _:
                pass

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #2's answer:", counts)
    print("=" * 10)


if __name__ == "__main__":
    solve_puzzle_one("./input/test")
    solve_puzzle_two("./input/test")

    solve_puzzle_one("./input/input")
    solve_puzzle_two("./input/input")

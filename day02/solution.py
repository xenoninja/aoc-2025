from utils.read import read_file_by_line


def solve_puzzle_one(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    id_ranges = lines[0].split(",")
    invalid_count = 0

    for id_range in id_ranges:
        [fst_id, lst_id] = id_range.split("-")
        fst_id = int(fst_id)
        lst_id = int(lst_id)
        for id in range(fst_id, lst_id + 1):
            id_str = str(id)
            id_len = len(id_str)
            if id_len % 2 == 0:
                half_len = int(id_len / 2)
                if id_str[:half_len] == id_str[half_len:]:
                    invalid_count += id

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #1's answer:", invalid_count)
    print("=" * 10)


def solve_puzzle_two(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    id_ranges = lines[0].split(",")
    invalid_count = 0

    for id_range in id_ranges:
        [fst_id, lst_id] = id_range.split("-")
        fst_id = int(fst_id)
        lst_id = int(lst_id)
        for id in range(fst_id, lst_id + 1):
            id_str = str(id)
            id_len = len(id_str)
            for i in range(2, id_len + 1):
                if id_len % i == 0:
                    idx = int(id_len / i)
                    if id_str[:idx] * i == id_str:
                        invalid_count += id
                        break

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #2's answer:", invalid_count)
    print("=" * 10)


if __name__ == "__main__":
    solve_puzzle_one("./input/test")
    solve_puzzle_two("./input/test")

    solve_puzzle_one("./input/input")
    solve_puzzle_two("./input/input")

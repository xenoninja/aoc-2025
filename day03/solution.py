from utils.read import read_file_by_line


def solve_puzzle_one(input_file):
    lines = read_file_by_line(input_file)
    total_joltage = 0

    for bank in lines:
        batteries = [int(battery) for battery in bank]
        cur_max_joltage = 0

        fst_battery = max(batteries[: len(batteries) - 1])

        for i in range(len(batteries) - 1):
            if batteries[i] == fst_battery:
                snd_battery = max(batteries[i + 1 :])
                tmp_joltage = fst_battery * 10 + snd_battery
                if tmp_joltage > cur_max_joltage:
                    cur_max_joltage = tmp_joltage

        total_joltage += cur_max_joltage

    print("Puzzle #1's answer:", total_joltage)


def solve_puzzle_two(input_file):
    lines = read_file_by_line(input_file)
    total_joltage = 0

    for bank in lines:
        batteries = [int(battery) for battery in bank]
        start_idx = 0
        digits_left = 12
        cur_joltage = 0
        max_lists = list()

        find_max_joltage(batteries, start_idx, digits_left, cur_joltage, max_lists)

        total_joltage += max(max_lists)

    print("Puzzle #2's answer:", total_joltage)


def find_max_joltage(batteries, start_idx, digits_left, cur_joltage, max_lists):
    max_battery = max(batteries[start_idx : len(batteries) - digits_left + 1])

    for i in range(start_idx, len(batteries) - digits_left + 1):
        if batteries[i] == max_battery:
            start_idx = i + 1
            digits_left -= 1
            cur_joltage = cur_joltage * 10 + max_battery
            if digits_left == 0:
                max_lists.append(cur_joltage)
            elif digits_left > 0:
                find_max_joltage(
                    batteries, start_idx, digits_left, cur_joltage, max_lists
                )


if __name__ == "__main__":
    solve_puzzle_one("./input/test")
    solve_puzzle_one("./input/input")

    solve_puzzle_two("./input/test")
    solve_puzzle_two("./input/input")

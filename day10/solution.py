from utils.read import read_file_by_line
import re
from itertools import combinations_with_replacement


def solve_puzzle_one(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    goals = []
    selections = []
    total_moves = 0

    for line in lines:
        goals = list()
        selections = list()
        goals_str = re.findall(r"\[(.*?)\]", line)[0]
        selections_str = re.findall(r"\((.*?)\)", line)
        for c in goals_str:
            if c == ".":
                n = 0
            else:
                n = 1
            goals.append(n)
        for c in selections_str:
            n = list(map(int, c.split(",")))
            selections.append(n)

        is_complete = False
        moves = 0

        while not is_complete:
            moves += 1

            for steps in list(
                combinations_with_replacement(range(len(selections)), moves)
            ):
                is_complete = True

                cur = []
                for i in range(len(goals)):
                    cur.append(0)
                for i in steps:
                    for j in selections[i]:
                        cur[j] += 1
                for i, n in enumerate(cur):
                    if (n % 2) != goals[i]:
                        is_complete = False
                        break
                if is_complete:
                    break

            if is_complete:
                break

        total_moves += moves

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #1's answer:", total_moves)
    print("=" * 10)


def solve_puzzle_two(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    goals = []
    selections = []
    total_moves = 0

    cnt = 0

    for line in lines:
        cnt += 1
        print(cnt)
        selections = list()
        goals_str = re.findall(r"\{(.*?)\}", line)[0]
        selections_str = re.findall(r"\((.*?)\)", line)
        goals = list(map(int, goals_str.split(",")))
        for c in selections_str:
            n = list(map(int, c.split(",")))
            selections.append(n)

        moves = 0

        total_moves += moves

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #2's answer:", total_moves)
    print("=" * 10)


if __name__ == "__main__":
    # solve_puzzle_one("./input/test")
    solve_puzzle_two("./input/test")

    # solve_puzzle_one("./input/input")
    solve_puzzle_two("./input/input")

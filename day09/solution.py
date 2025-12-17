from utils.read import read_file_by_line
from shapely.geometry import Polygon, box
from itertools import combinations


def solve_puzzle_one(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    points = []

    for line in lines:
        pos_str = line.split(",")
        coordinates = [int(pos_str[0]), int(pos_str[1])]
        points.append(coordinates)

    max_res = 0

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            res = (points[i][0] - points[j][0] + 1) * (points[i][1] - points[j][1] + 1)

            if res > max_res:
                max_res = res

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #1's answer:", max_res)
    print("=" * 10)


def solve_puzzle_two(input_file):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    def area(edge) -> int:
        ((x1, y1), (x2, y2)) = edge
        return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

    points = []
    for line in lines:
        x, y = map(int, line.split(","))
        points.append((x, y))

    polygon = Polygon(points)
    for edge in sorted(combinations(points, 2), key=area, reverse=True):
        (x1, y1), (x2, y2) = edge
        if polygon.contains(box(x1, y1, x2, y2)):
            res = area(edge)
            break

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #2's answer:", res)
    print("=" * 10)


if __name__ == "__main__":
    solve_puzzle_one("./input/test")
    solve_puzzle_two("./input/test")

    solve_puzzle_one("./input/input")
    solve_puzzle_two("./input/input")

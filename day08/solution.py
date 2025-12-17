from operator import itemgetter
from utils.read import read_file_by_line, raw_read_file_by_line


class Position:
    def __init__(self, str, group_id):
        coordinates = str.split(",")
        self.x = int(coordinates[0])
        self.y = int(coordinates[1])
        self.z = int(coordinates[2])
        self.group_id = group_id

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}, group_id: {self.group_id}\n"

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}, group_id: {self.group_id}\n"


def calc_distance(pos_1, pos_2):
    return (
        (pos_1.x - pos_2.x) ** 2 + (pos_1.y - pos_2.y) ** 2 + (pos_1.z - pos_2.z) ** 2
    ) ** 0.5


def solve_puzzle_one(input_file, connections_cnt):
    lines = read_file_by_line(input_file)

    if lines is None:
        return

    boxes = list()
    connected_boxes = set()
    distances = list()

    for i in range(len(lines)):
        boxes.append(Position(lines[i], i))

    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            dis = calc_distance(boxes[i], boxes[j])
            distances.append((dis, i, j))

    distances.sort(key=itemgetter(0))

    for i in range(connections_cnt):
        (_, cur_box_1, cur_box_2) = distances[i]
        min_group_id = min(boxes[cur_box_1].group_id, boxes[cur_box_2].group_id)
        max_group_id = max(boxes[cur_box_1].group_id, boxes[cur_box_2].group_id)

        for box in boxes:
            if box.group_id == max_group_id:
                box.group_id = min_group_id
                connected_boxes.add(box)

    res = 1
    box_group_dicts = dict()
    box_group_counts = list()

    for box in boxes:
        if box.group_id in box_group_dicts:
            box_group_dicts[box.group_id] += 1
        else:
            box_group_dicts[box.group_id] = 1

    for i in box_group_dicts:
        box_group_counts.append(box_group_dicts[i])

    box_group_counts.sort(reverse=True)

    for i in range(3):
        res *= box_group_counts[i]

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #1's answer:", res)
    print("=" * 10)


def solve_puzzle_two(input_file):
    lines = raw_read_file_by_line(input_file)

    if lines is None:
        return

    boxes = list()
    connected_boxes = set()
    distances = list()

    for idx in range(len(lines)):
        boxes.append(Position(lines[idx], idx))

    for idx in range(len(boxes)):
        for j in range(idx + 1, len(boxes)):
            dis = calc_distance(boxes[idx], boxes[j])
            distances.append((dis, idx, j))

    distances.sort(key=itemgetter(0))

    idx = 0
    while True:
        (_, cur_box_1, cur_box_2) = distances[idx]
        idx += 1
        min_group_id = min(boxes[cur_box_1].group_id, boxes[cur_box_2].group_id)
        max_group_id = max(boxes[cur_box_1].group_id, boxes[cur_box_2].group_id)

        for box in boxes:
            if box.group_id == max_group_id:
                box.group_id = min_group_id
                connected_boxes.add(box)

        end_flag = True
        for box in boxes:
            if box.group_id != 0:
                end_flag = False

        if end_flag:
            res = boxes[cur_box_1].x * boxes[cur_box_2].x
            break

    print("=" * 10)
    print("Input file:", input_file)
    print("Puzzle #2's answer:", res)
    print("=" * 10)


if __name__ == "__main__":
    solve_puzzle_one("./input/test", 10)
    solve_puzzle_two("./input/test")

    solve_puzzle_one("./input/input", 1000)
    solve_puzzle_two("./input/input")

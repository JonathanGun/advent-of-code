import re
from functools import reduce
from collections import Counter

SAMPLE = False

filename = "input/sample.in" if SAMPLE else "input/star.in"

# sample: p=9,5 v=-3,-3
regex = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
robot_positions = []
robot_velocities = []
with open(filename) as f:
    for line in f.readlines():
        m = re.match(regex, line.strip())
        robot_positions.append(tuple(map(int, m.groups()[:2][::-1])))
        robot_velocities.append(tuple(map(int, m.groups()[2:][::-1])))
# print(robot_positions)
# print(robot_velocities)


def get_quadrant(pos, r, c):
    if pos[0] == (r - 1) // 2 or pos[1] == (c - 1) // 2:
        return None
    if pos[0] < r // 2:
        if pos[1] < c // 2:
            return 1
        else:
            return 2
    else:
        if pos[1] < c // 2:
            return 3
        else:
            return 4


def count_safety_factor(robot_positions, r, c):
    robots_per_quadrant = [0, 0, 0, 0]
    for pos in robot_positions:
        quadrant = get_quadrant(pos, r, c)
        if quadrant is not None:
            robots_per_quadrant[quadrant - 1] += 1
    return reduce(lambda x, y: x * y, robots_per_quadrant)


def move(pos, vel, r, c, n=1):
    return (
        (pos[0] + n * vel[0]) % r,
        (pos[1] + n * vel[1]) % c,
    )


def print_grid(robot_positions, r, c):
    counter = Counter(robot_positions)
    for i in range(r):
        for j in range(c):
            if (i, j) in robot_positions:
                print(counter[(i, j)], end="")
            else:
                print(".", end="")
        print()
    print()


R = 7 if SAMPLE else 103
C = 11 if SAMPLE else 101
N = len(robot_positions)
moves = 100

for j in range(N):
    robot_positions[j] = move(robot_positions[j], robot_velocities[j], R, C, moves)
# print_grid(robot_positions, R, C)
print(count_safety_factor(robot_positions, R, C))

for j in range(N):
    robot_positions[j] = move(robot_positions[j], robot_velocities[j], R, C, -moves)

moves = 1000000
threshold = 3 if SAMPLE else 20
candidates = 1
cnt = 0
# print_grid(robot_positions, R, C)
for n in range(moves):
    for j in range(N):
        robot_positions[j] = move(robot_positions[j], robot_velocities[j], R, C, 1)

    # find when lot of robots are next to each other in a row
    robots_by_row = [[] for _ in range(R)]
    for pos in robot_positions:
        robots_by_row[pos[0]].append(pos[1])
    robots_by_row = [sorted(row) for row in robots_by_row]
    # print(robots_by_row)

    # find diff with next element in each row
    diffs = []
    for row in robots_by_row:
        tmp = []
        for i in range(len(row) - 1):
            tmp.append(row[i + 1] - row[i])
        diffs.append(Counter(tmp))
    # print(diffs)

    for diff in diffs:
        if diff.get(1, 0) >= threshold:
            print_grid(robot_positions, R, C)
            print(n + 1)
            cnt += 1
            break

    if cnt >= candidates:
        break

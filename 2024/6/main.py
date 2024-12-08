SAMPLE = False

filepath = "input/sample.in" if SAMPLE else "input/star.in"


def get_pos(grid, coord):
    if (
        coord[0] < 0
        or coord[1] < 0
        or coord[0] >= len(grid)
        or coord[1] >= len(grid[0])
    ):
        return None
    return grid[coord[0]][coord[1]]


def move(coord, dist):
    return (coord[0] + dist[0], coord[1] + dist[1])


def turn(cur_dir):
    next_dir = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
    }
    return next_dir[cur_dir]


def get_next_cell(grid, cur_pos, cur_dir, added_obstacle_pos=None):
    next_pos = move(cur_pos, cur_dir)
    next_cell = get_pos(grid, next_pos)
    next_dir = cur_dir
    if next_cell == "#" or next_pos == added_obstacle_pos:
        next_dir = turn(cur_dir)
        next_pos = move(cur_pos, next_dir)
        next_cell = get_pos(grid, next_pos)
    return next_cell, next_pos, next_dir


def readfile(filepath):
    grid = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    return grid


def get_start_pos(grid, start_char="^"):
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "^":
                return (i, j)
    return None


def count_steps(grid, start_pos, cur_dir=(-1, 0), added_obstacle_pos=None):
    cur_pos = get_start_pos(grid)
    visited = set()
    is_stuck_in_loop = False
    MAX_ITER = 1_000_000
    i = 0
    while i < MAX_ITER:
        i += 1
        visited.add((cur_pos, cur_dir))
        next_cell, next_pos, next_dir = get_next_cell(
            grid, cur_pos, cur_dir, added_obstacle_pos
        )
        if (next_pos, next_dir) in visited:
            is_stuck_in_loop = (cur_pos, cur_dir)
            # print((cur_pos, cur_dir), "->", (next_pos, next_dir))
            break
        if next_cell is None:
            break
        cur_pos = next_pos
        cur_dir = next_dir
    if i == MAX_ITER:
        exit(1)
    return visited, is_stuck_in_loop


def get_unique_pos(visited):
    unique_pos = set()
    for pos, _ in visited:
        unique_pos.add(pos)
    return unique_pos


def print_board(grid, visited=None, added_obstacle_pos=None, stuck_info=None):
    if not visited:
        visited = set()
    stuck_pos, _ = stuck_info
    unique_pos = get_unique_pos(visited)
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if (i, j) == stuck_pos:
                print("S", end="")
            elif c == "^":
                print("^", end="")
            elif (i, j) in unique_pos:
                print("o", end="")
            elif (i, j) == added_obstacle_pos:
                print("x", end="")
            else:
                print(c, end="")
        print()
    print()


grid = readfile(filepath)

# part one
visited, is_stuck_in_loop = count_steps(grid, get_start_pos(grid))
unique_pos = get_unique_pos(visited)
print(len(unique_pos))

# # part two
# cnt = 0
# for i, row in enumerate(grid):
#     for j, c in enumerate(row):
#         if c == "#" or c == "^":
#             continue
#         visited, is_stuck_in_loop = count_steps(
#             grid, get_start_pos(grid), added_obstacle_pos=(i, j)
#         )
#         if is_stuck_in_loop:
#             cnt += 1
#             print((i, j), "loop in", is_stuck_in_loop)
#             # print_board(grid, visited, (i, j), is_stuck_in_loop)
# print(cnt)

# Part Two
cnt = 0  # Counter for valid obstruction positions

# Iterate over every cell in the grid
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        # Skip positions that are walls or the starting position
        if c == "#" or (i, j) == get_start_pos(grid):
            continue

        # Simulate with an added obstruction at (i, j)
        visited, is_stuck_in_loop = count_steps(
            grid, get_start_pos(grid), added_obstacle_pos=(i, j)
        )

        # If the guard gets stuck in a loop, increment the counter
        if is_stuck_in_loop:
            cnt += 1
            # Debugging: Print the grid with the obstruction
            # print_board(grid, visited, (i, j), is_stuck_in_loop)

print(cnt)  # Output the total number of valid positions

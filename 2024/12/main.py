from collections import defaultdict
from typing import List
import sys

sys.setrecursionlimit(100000)

SAMPLE = False

filename = "input/sample.in" if SAMPLE else "input/star.in"

grid = []
with open(filename) as f:
    for line in f.readlines():
        grid.append(["."] + list(line.strip()) + ["."])
grid = (
    [["." for _ in range(len(grid[0]))]] + grid + [["." for _ in range(len(grid[0]))]]
)
# for row in grid:
#     print(row)
# print()

visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
regions = defaultdict(set)


# return area, perimeter
def floodfill(grid, start: (int, int), cur: str, r: int, c: int, visited) -> (int, int):
    if (
        r < 1
        or c < 1
        or r >= len(grid) - 1
        or c >= len(grid[0]) - 1
        or grid[r][c] != cur
    ):
        return 0, 1
    if visited[r][c]:
        return 0, 0

    visited[r][c] = True
    area, perimeter = 1, 0
    regions[start].add((r, c))
    # print(area, perimeter)
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if abs(i + j) != 1:
                continue
            # print(r + i, c + j)
            a, p = floodfill(grid, start, cur, r + i, c + j, visited)
            area += a
            perimeter += p
    return area, perimeter


ans = 0
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if r == 0 or c == 0 or r == len(grid) - 1 or c == len(grid[0]) - 1:
            continue
        if not visited[r][c]:
            # print(r, c, cell, floodfill(cell, r, c))
            a, p = floodfill(grid, (r, c), cell, r, c, visited)
            # print(a, p)
            ans += a * p
print(ans)

# part 2, mimic line follower algorithm


def turn_left(d: (int, int)) -> (int, int):
    return {
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (0, -1): (1, 0),
        (1, 0): (0, 1),
    }.get(d)


def turn_right(d: (int, int)) -> (int, int):
    return {
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
    }.get(d)


def move_forward(r: int, c: int, d: (int, int)) -> (int, int):
    return r + d[0], c + d[1]


def get_front_cell(grid, r: int, c: int, d: (int, int)) -> (int, int):
    r, c = move_forward(r, c, d)
    return grid[r][c]


def line_follower_step(
    grid, cur: str, left: (int, int), right: (int, int), d: (int, int)
) -> ((int, int), (int, int), (int, int)):
    rr, rc = right
    lr, lc = left
    # print(right, left, d)
    if get_front_cell(grid, rr, rc, d) != cur:
        # print("R nabrak, belok kanan")
        left = move_forward(rr, rc, d)
        d = turn_right(d)
    elif get_front_cell(grid, lr, lc, d) == cur:
        # print("L nabrak, belok kiri")
        right = move_forward(lr, lc, d)
        d = turn_left(d)
    else:
        right = move_forward(rr, rc, d)
        left = move_forward(lr, lc, d)
    return left, right, d


# side_cache = {}


def sides(grid, start: (int, int), start_d: (int, int)) -> (int, int):
    # if start in side_cache:
    #     return side_cache[start]

    side_cnt = 0

    right = start
    rr, rc = right
    left = (rr - 1, rc)
    d = start_d

    visited_cells = set()
    while True:
        # for r, row in enumerate(grid):
        #     for c, cell in enumerate(row):
        #         rr, rc = right
        #         lr, lc = left
        #         if r == rr and c == rc:
        #             print("R", end="")
        #         elif r == lr and c == lc:
        #             print("L", end="")
        #         else:
        #             print(cell, end="")
        #     print()
        # print()

        visited_cells.add(left)
        visited_cells.add(right)
        rr, rc = right
        prev_d = d
        left, right, d = line_follower_step(grid, grid[rr][rc], left, right, d)

        if prev_d != d:
            side_cnt += 1
        if right == start and d == start_d:
            break
    # side_cache[start] = (side_cnt, visited_cells)
    return side_cnt, visited_cells


def get_region_hole(grid, start, visited_cells, region_cells):
    region_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for r, c in region_cells:
        region_grid[r][c] = 1
    # for row in region_grid:
    #     print(row)
    # print()
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for cell in visited_cells:
        r, c = cell
        if not visited[r][c]:
            floodfill(region_grid, (r, c), region_grid[r][c], r, c, visited)

    min_r, max_r, min_c, max_c = bounding_boxes[start]
    for r in range(min_r, max_r + 1):
        for c in [min_c, max_c]:
            if not visited[r][c]:
                floodfill(region_grid, (r, c), region_grid[r][c], r, c, visited)
    for c in range(min_c, max_c + 1):
        for r in [min_r, max_r]:
            if not visited[r][c]:
                floodfill(region_grid, (r, c), region_grid[r][c], r, c, visited)

    # for row in region_grid:
    #     print(row)
    # print()
    # for row in visited:
    #     print(list(map(lambda vis: "X" if vis else ".", row)))
    # print()
    # print(min_r, max_r, min_c, max_c)
    hole = 0
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if not visited[r][c]:
                floodfill(region_grid, (r, c), region_grid[r][c], r, c, visited)
                cnt, v = sides(region_grid, (r, c), (0, 1))
                # print("line following", (r, c), cnt, v)
                hole += cnt
    return hole


# def get_region_hole(
#     r: int, c: int, cells: set((int, int))
# ) -> set(((int, int), (int, int))):
#     # print("checking region", r, c)
#     min_r, max_r, min_c, max_c = bounding_boxes[(r, c)]
#     region_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
#     for r in range(min_r, max_r + 1):
#         for c in range(min_c, max_c + 1):
#             if (r, c) in cells:
#                 region_grid[r][c] = 1
#     # for row in region_grid:
#     #     print(row)
#     # print()

#     visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
#     for r in range(min_r, max_r + 1):
#         for c in [min_c, max_c]:
#             if not visited[r][c]:
#                 floodfill(region_grid, (r, c), region_grid[r][c], r, c, visited)
#     for c in range(min_c, max_c + 1):
#         for r in [min_r, max_r]:
#             if not visited[r][c]:
#                 floodfill(region_grid, (r, c), region_grid[r][c], r, c, visited)
#     # for row in visited:
#     #     print(row)
#     # print()

#     cnt = 0
#     for r in range(min_r, max_r + 1):
#         for c in range(min_c, max_c + 1):
#             if not visited[r][c]:
#                 floodfill(region_grid, (r, c), region_grid[r][c], r, c, visited)
#                 cnt += sides((r, c), (0, 1))
#     # for row in region_grid:
#     #     print(row)
#     # print()
#     return cnt


region_copy = {region: cells.copy() for region, cells in regions.items()}
bounding_boxes = {}
for region, cells in region_copy.items():
    min_r = min(c[0] for c in cells)
    max_r = max(c[0] for c in cells)
    min_c = min(c[1] for c in cells)
    max_c = max(c[1] for c in cells)
    bounding_boxes[region] = (min_r, max_r, min_c, max_c)


# # print(regions)
# print(len(regions))
# print(get_region_hole(grid))
# # max length of value of region
# print(max([len(v) for v in regions.values()]))

visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

ans = 0
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if r == 0 or c == 0 or r == len(grid) - 1 or c == len(grid[0]) - 1:
            continue
        if not visited[r][c]:
            # print(i, j, cell, floodfill(cell, i, j))
            a, _ = floodfill(grid, (r, c), cell, r, c, visited)
            # print(regions[(r, c)])
            s, vis_cells = sides(grid, (r, c), (0, 1))
            h = get_region_hole(grid, (r, c), vis_cells, regions[(r, c)])
            # s += get_region_hole(r, c, region_copy[(r, c)])
            print(r, c, cell, a, s + h, s, h)
            ans += a * (s + h)
# print(side_cache)
print(ans)
# 834528 too high
# 834896 too high
# 818936 wrong
# 818632 wrong
# 819056 wrong

import heapq
from collections import defaultdict


def read_grid(filename):
    grid = []
    with open(filename, "r") as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid


def print_grid(grid, path=None):
    if path is None:
        path = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) in path:
                print("O", end="")
            else:
                print(cell, end="")
        print()
    print()


def get_start_end(grid):
    start, end = None, None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                start = (i, j)
            elif cell == "E":
                end = (i, j)
    return start, end


def get_neighbors(grid, cur):
    neighbors = []
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if abs(i + j) != 1:
                continue
            if grid[cur[0] + i][cur[1] + j] == "#":
                continue
            neighbors.append((cur[0] + i, cur[1] + j))
    return neighbors


def get_direction(cur, neighbor):
    return (
        neighbor[0] - cur[0],
        neighbor[1] - cur[1],
    )


def count_cell_in_path(parents, leaf) -> int:
    print(leaf, parents[leaf])
    if not parents[leaf]:
        return 1
    return sum(count_cell_in_path(parents, parent) for parent in parents[leaf]) + 1


TURN_WEIGHT = 1000

if __name__ == "__main__":
    SAMPLE = False

    filename = "input/sample.in" if SAMPLE else "input/star.in"
    grid = read_grid(filename)

    # print_grid(grid)

    start, end = get_start_end(grid)

    # (priority, position, direction, previous_pos)
    queue = [(0, start, (0, 1), None)]
    heapq.heapify(queue)
    visited = set()
    parents = defaultdict(list)
    prios = {}
    prios2 = {}
    while queue:
        prio, cur, d, prev = heapq.heappop(queue)
        print("checking", prio, cur, d)

        if (cur, d) in visited:
            continue

        visited.add((cur, d))
        if cur in prios:
            prios[cur] = min(prio, prios[cur])
        else:
            prios[cur] = prio
        if prev is not None:
            if prev not in prios2:
                prios2[prev] = prio - 1
            else:
                prios2[prev] = min(prio - 1, prios2[prev])

        if cur == end:
            break

        neighbors = get_neighbors(grid, cur)
        for neighbor in neighbors:
            next_d = get_direction(cur, neighbor)
            next_prio = prio
            if d != next_d:
                next_prio += TURN_WEIGHT
                if d[0] == next_d[0] or d[1] == next_d[1]:
                    next_prio += TURN_WEIGHT
                neighbor = cur
            else:
                next_prio += 1

            print("adding to queue", next_prio, neighbor, next_d, cur)
            heapq.heappush(queue, (next_prio, neighbor, next_d, cur))

    else:
        print("not found")
    print_grid(grid)
    print(prio)
    # print(parents[end])
    # for k, v in parents.items():
    #     print(k, v)

    # print prios
    for pos, prio in sorted(prios.items(), key=lambda x: x[1]):
        print(pos, prio)
    for pos, prio in sorted(prios2.items(), key=lambda x: x[1]):
        print(pos, prio)

    ans = set()
    d = (next_d[0] * -1, next_d[1] * -1)
    print(d)
    queue = [(-prio, end, d)]
    prio2 = {}
    while queue:
        prio, cur, d = heapq.heappop(queue)
        prio = -prio
        print("checking", prio, cur)

        if (cur, d) not in prio2:
            prio2[(cur, d)] = prio
        if cur in ans:
            continue

        ans.add((cur, d))
        cur = (cur[0] + d[0], cur[1] + d[1])
        if 0 <= cur[0] < len(grid) and 0 <= cur[1] < len(grid[0]) and grid[cur[0]][cur[1]] != "#":
            heapq.heappush(queue, (-prio, cur, d))
    # for cur in sorted(ans):
    #     print(cur)
    print_grid(grid, ans)
    # print(count_cell_in_path(parents, end))

from collections import deque

SAMPLE = False

filename = "input/sample.in" if SAMPLE else "input/star.in"

peaks = deque()
grid = []
with open(filename) as f:
    for line in f.readlines():
        grid.append(list(map(lambda c: int(c) if c != '.' else -999, line.strip())))
# for row in grid:
#     print(row)
# print()

reachable = [[set() for _ in range(len(grid[0]))] for _ in range(len(grid))]
ways = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == 9:
            ways[i][j] = 1
            peaks.append((i, j))
            reachable[i][j].add((i, j))
# print(peaks)

visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
trailheads = []
while peaks:
    r, c = peaks.popleft()
    if visited[r][c]:
        continue
    visited[r][c] = True
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if abs(i + j) == 1:
                if 0 <= r + i < len(grid) and 0 <= c + j < len(grid[0]) and grid[r + i][c + j] == grid[r][c] - 1:
                    peaks.append((r + i, c + j))
                    # print(f"Adding peak at {(r, c)} + ({i}, {j}) = {(r + i, c + j)}")
                    ways[r + i][c + j] += ways[r][c]
                    reachable[r + i][c + j] = reachable[r + i][c + j].union(reachable[r][c])
    if grid[r][c] == 0:
        trailheads.append((r, c))
# print(trailheads)
# for row in ways:
#     print(row)
# print()

ans = 0
ans2 = 0
for trailhead in trailheads:
    r, c = trailhead
    ans2 += ways[r][c]
    ans += len(reachable[r][c])
print(ans)
print(ans2)

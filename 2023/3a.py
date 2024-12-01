grid = []
with open("3.in") as f:
    for line in f:
        grid.append(list(line.strip()))
# print(grid)
R = len(grid)
C = len(grid[0])
vis = [[False for j in range(C)] for i in range(R)]

def ff(r, c):
    if not (0 <= r < R and 0 <= c < C):
        return
    if vis[r][c]:
        return
    if not ('0' <= grid[r][c] <= '9'):
        return
    vis[r][c] = True
    ff(r, c - 1)
    ff(r, c + 1)


for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if not ('0' <= char <= '9' or char == '.'):
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    ff(r + i, c + j)

ans = 0
for r, row in enumerate(grid):
    num = ''
    last = None
    for c, char in enumerate(row):
        if vis[r][c]:
            num += grid[r][c]
            last = True
        else:
            if last:
                print(r, c, num)
                ans += int(num)
                num = ''
            last = False
    if last:
        print(r, c, num)
        ans += int(num)
        num = ''
    last = False

# for i in range(len(grid)):
#     print(grid[i])
#     print(vis[i])
print(ans)

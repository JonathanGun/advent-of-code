# from S, follow each direction (north, east, south, west) until you reach back to S
# if you can follow and reach back to S, then it is a loop. Otherwise, it is not a loop.
# the answer is the loop length / 2

filename = "10.in"

charToDir = {
    "-": [(0, 1), (0, -1)],
    "|": [(-1, 0), (1, 0)],
    "L": [(0, 1), (-1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
}

def move(coord1, d):
    return (coord1[0] + d[0], coord1[1] + d[1])

grid = []
start_coord = (-1, -1)
with open(filename) as f:
    r = 0
    for line in f.readlines():
        line = list(line.strip())
        grid.append(line)
        for c, ch in enumerate(line):
            if ch == "S":
                start_coord = (r, c)
        r += 1

# for g in grid:
#     print(g)

print("start", start_coord)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for d in dirs:
    # print("trying dir", d)
    prev_coord = start_coord
    cur_coord = move(start_coord, d)
    length = 1
    while cur_coord != start_coord:
        # print("now at", cur_coord, "char", grid[cur_coord[0]][cur_coord[1]])
        cur_char = None
        try:
            cur_char = grid[cur_coord[0]][cur_coord[1]]
        except Exception as e:
            break
        if cur_char == ".":
            break

        connected = False
        for dd in charToDir[cur_char]:
            # print("checking dir", dd, "from", cur_coord, "to", move(cur_coord, dd), "is it equal to", prev_coord, move(cur_coord, dd) == prev_coord)
            if move(cur_coord, dd) == prev_coord:
                connected = True
                break
        if not connected:
            print("not connected")
            break

        for dd in charToDir[cur_char]:
            if move(cur_coord, dd) != prev_coord:
                prev_coord = cur_coord
                cur_coord = move(cur_coord, dd)
                # print("move", dd, "to", cur_coord)
                break
        length += 1
    else:
        print("loop length", length // 2)
        break

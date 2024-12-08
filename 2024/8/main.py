SAMPLE = False

filename = "input/sample.in" if SAMPLE else "input/star.in"


def get_antinodes(r1, c1, r2, c2, n, is_part_one=True):
    dr = r2 - r1
    dc = c2 - c1
    cur_r, cur_c = r1, c1
    if is_part_one:
        cur_r -= dr
        cur_c -= dc
    while valid_pos((cur_r, cur_c), n):
        yield (cur_r, cur_c)
        cur_r -= dr
        cur_c -= dc
        if is_part_one:
            break
    cur_r, cur_c = r2, c2
    if is_part_one:
        cur_r += dr
        cur_c += dc
    while valid_pos((cur_r, cur_c), n):
        yield (cur_r, cur_c)
        cur_r += dr
        cur_c += dc
        if is_part_one:
            break


def valid_pos(pos, n):
    return 0 <= pos[0] < n and 0 <= pos[1] < n


grid = []
unique_frequencies = set()
with open(filename) as f:
    for line in f.readlines():
        ls = list(line.strip())
        grid.append(ls)
        unique_frequencies.update(ls)
unique_frequencies.remove(".")
# print(grid)
# print(unique_frequencies)

# O((r*c)^2) solution
antennas = {}
for frequency in unique_frequencies:
    antennas[frequency] = []
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == frequency:
                antennas[frequency].append((r, c))
# print(antennas)

antinodes = set()
antinodes2 = set()
for frequency, positions in antennas.items():
    for i, (r1, c1) in enumerate(positions):
        for j, (r2, c2) in enumerate(positions):
            if i == j:
                continue
            for antinode in get_antinodes(r1, c1, r2, c2, len(grid)):
                antinodes.add(antinode)
            for antinode in get_antinodes(r1, c1, r2, c2, len(grid), False):
                antinodes2.add(antinode)
# print(len(all_antinodes), sorted(all_antinodes))
# print(len(antinodes), sorted(antinodes))

# for r, row in enumerate(grid):
#     for c, cell in enumerate(row):
#         if (r, c) in antinodes2:
#             print("#", end="")
#         else:
#             print(cell, end="")
#     print()
# print()

print(len(antinodes))
print(len(antinodes2))

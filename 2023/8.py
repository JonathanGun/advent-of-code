from math import lcm

instruction = list(input())
input()

grid = {}
nodes = []
while inp := input():
    start, left, right = inp.replace("= (", " ").replace(",", "").replace(")", "").split()
    if start[-1] == 'A':
        nodes.append(start)
    grid[start] = [left, right]

nearest = []
for i in range(len(nodes)):
    steps = 0
    found = False
    cur = nodes[i]
    while not found:
        for ins in instruction:
            steps += 1
            cur = grid[cur][0 if ins == 'L' else 1]
        if cur[-1] == 'Z':
            nearest.append(steps)
            found = True
            break

print(nearest)
print(lcm(*nearest))

seeds = list(map(int, input().split()))
input()

maps = []
NO_OF_MAPS = 7

for _ in range(NO_OF_MAPS):
    maps.append([])
    while True:
        x = input()
        if not x:
            break
        dest, source, rng = map(int, x.split())
        maps[-1].append([source, dest, rng])

for mp in maps:
    mp.sort()

print(seeds)
locations = []
for j, mp in enumerate(maps):
    for i, seed in enumerate(seeds):
        for src, dst, rng in mp:
            if src <= seed <= src + rng - 1:
                seeds[i] = dst + (seed - src)
                break
        print(i, dst, src, rng, seed, "become", seeds[i])
    print(j, seeds)
print(min(seeds))

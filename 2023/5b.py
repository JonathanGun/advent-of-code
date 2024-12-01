seeds_ = list(map(int, input().split()))
input()
# seeds_ = list(range(101))

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

print(seeds_)
seeds = []
for i in range(len(seeds_) // 2):
    print(i, seeds_[i * 2], seeds_[i * 2 + 1])
    seeds.extend(range(seeds_[i * 2], seeds_[i * 2] + seeds_[i * 2 + 1]))
seeds = list(set(seeds))
print(len(seeds))

locations = []
for j, mp in enumerate(maps):
    for i, seed in enumerate(seeds):
        for src, dst, rng in mp:
            if src <= seed <= src + rng - 1:
                seeds[i] = dst + (seed - src)
                break
    #     print(i, dst, src, rng, seed, "become", seeds[i])
    # print(j, seeds)
print(min(seeds))

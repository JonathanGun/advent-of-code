# times = [71530]
# distances = [940200]

times = [48989083]
distances = [390110311121360]

ans = 1
for i, time in enumerate(times):
    cnt = 0
    # O(time)
    for charge_time in range(1, time):
        move_time = time - charge_time
        dist = move_time * charge_time
        if dist > distances[i]:
            cnt += 1
    ans *= cnt
print(ans)

# times = [7, 15, 30]
# distances = [9, 40, 200]

times = [48, 98, 90, 83]
distances = [390, 1103, 1112, 1360]

ans = 1
for i, time in enumerate(times):
    cnt = 0
    for charge_time in range(1, time):
        move_time = time - charge_time
        dist = move_time * charge_time
        if dist > distances[i]:
            cnt += 1
    ans *= cnt
print(ans)

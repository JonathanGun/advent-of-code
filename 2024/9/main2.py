from typing import List
from queue import PriorityQueue as pq
from collections import defaultdict

SAMPLE = True

filename = "input/sample.in" if SAMPLE else "input/star.in"

s = ""
with open(filename) as f:
    for line in f.readlines():
        s = line.strip()
files = list(map(int, s[0::2]))
spaces = list(map(int, s[1::2]))
# print(files)
# print(spaces)

debug_str = ""


def _checksum(start: int, end: int, val: int):
    # global debug_str
    # print(
    #     start, "-", end, "(", val, ") =", (start + end) * (end - start + 1) // 2 * val
    # )
    # print(str(val) * (end - start + 1))
    # debug_str += str(val) * (end - start + 1)
    return (start + end) * (end - start + 1) // 2 * val


# def checksum(
#     files: List[int],
#     spaces: List[int],
#     cur_disk: int,
#     last_disk: int,
#     next_space_cnt: int,
#     last_disk_cnt: None,
#     i: int,
# ):
#     cur_disk_cnt = files[cur_disk]

#     print("start", i)
#     # print(cur_disk_cnt)
#     if cur_disk_cnt < 0:
#         return 0
#     if cur_disk > last_disk:
#         return 0
#     if cur_disk == last_disk:
#         # print("cur_disk", cur_disk, "== last_disk", last_disk)
#         return _checksum(i, i + last_disk_cnt - 1, cur_disk)
#     print("depan", cur_disk_cnt, "angkanya:", cur_disk)
#     cur_checksum = _checksum(i, i + cur_disk_cnt - 1, cur_disk)
#     i += cur_disk_cnt
#     # print(cur_checksum)
#     MAX_ITER = 1_000_000_000
#     x = 0
#     # print("sisa kosong:", next_space_cnt)
#     while next_space_cnt > 0 and x < MAX_ITER:
#         x += 1
#         if last_disk_cnt > next_space_cnt:
#             # print("blkgnya", last_disk_cnt, "is greater than sisa", next_space_cnt)
#             # cur_checksum += next_space_cnt * last_disk
#             cur_checksum += _checksum(i, i + next_space_cnt - 1, last_disk)
#             i += next_space_cnt
#             last_disk_cnt -= next_space_cnt
#             cur_disk += 1
#             next_space_cnt = 0
#         else:
#             # cur_checksum += last_disk_cnt * last_disk
#             # print("last", last_disk_cnt)
#             cur_checksum += _checksum(i, i + last_disk_cnt - 1, last_disk)
#             i += last_disk_cnt
#             next_space_cnt -= last_disk_cnt
#             last_disk -= 1
#             last_disk_cnt = files[last_disk]
#             # print("sisa", next_space_cnt)
#             if next_space_cnt == 0:
#                 cur_disk += 1
#     if next_space_cnt == 0:
#         next_space_cnt = spaces[cur_disk]
#     print(cur_checksum)
#     return cur_checksum + checksum(
#         files, spaces, cur_disk, last_disk, next_space_cnt, last_disk_cnt, i
#     )

spaces.append(0)
n_files = len(files)
n_spaces = len(spaces)

# cur_file_id = 0
# last_file_id = n_files - 1
# checksum = 0
# i = 0
# while cur_file_id <= last_file_id:
#     cur_space = spaces[cur_file_id]
#     print(i)

#     # from left
#     # print("left==")
#     checksum += _checksum(i, i + files[cur_file_id] - 1, cur_file_id)
#     i += files[cur_file_id]

#     if cur_file_id == last_file_id:
#         break

#     # from right
#     # print("right==")
#     while cur_space > 0:
#         # print("space:", cur_space)
#         if files[last_file_id] >= cur_space:
#             checksum += _checksum(i, i + cur_space - 1, last_file_id)
#             i += cur_space
#             files[last_file_id] -= cur_space
#             cur_file_id += 1
#             cur_space = 0
#         else:
#             checksum += _checksum(i, i + files[last_file_id] - 1, last_file_id)
#             i += files[last_file_id]
#             cur_space -= files[last_file_id]
#             files[last_file_id] = 0
#             last_file_id -= 1

# print(debug_str)
# print(checksum)

# print(sum(map(int, list(s))))
arr_s = list(map(int, list(s)))
x = sum(arr_s)
arr = [0 for _ in range(x)]

cur = 0
for i in range(n_files):
    file = files[i]
    space = spaces[i]
    arr[cur : cur + file] = [i] * file
    cur += file
    arr[cur : cur + space] = [-1] * space
    cur += space

last = x - 1
i = 0
while i < last:
    if arr[i] == -1:
        arr[i] = arr[last]
        arr[last] = -1
        last -= 1
    else:
        i += 1

ans = 0
for i, v in enumerate(arr):
    if v == -1:
        continue
    ans += i * v
print(ans)

arr = [0 for _ in range(x)]
space_pos = defaultdict(pq)
file_pos = []
cur = 0
for i in range(n_files):
    file = files[i]
    space = spaces[i]
    file_pos.append(cur)
    for j in range(file):
        arr[cur] = i
        cur += 1
    space_pos[space].put(cur)
    for j in range(space):
        arr[cur] = -1
        cur += 1

# print(files, n_files)
# print(spaces, n_spaces)
# print(sorted(space_pos))
for i in range(n_files - 1, -1, -1):
    # print("moving file", i)
    file = files[i]
    space = spaces[i]

    # print("filesize", file)
    chosen_space = None
    cur_space = x
    for j in sorted(space_pos):
        if j < file:
            continue
        # cur_space = min(cur_space, space_pos[j].queue[0])
        if space_pos[j].empty():
            continue
        if space_pos[j].queue[0] < cur_space:
            cur_space = space_pos[j].queue[0]
            chosen_space = j
            # print("change to", j)

    if chosen_space is None:
        continue

    cur_space = space_pos[chosen_space].get()
    space_pos[chosen_space - file].put(cur_space + file)
    # print("move to location:", cur_space)

    arr[cur_space : cur_space + file] = [i] * file
    cur_file = file_pos[i]
    arr[cur_file : cur_file + file] = [-1] * file

ans = 0
for i, v in enumerate(arr):
    if v == -1:
        continue
    ans += i * v
print(ans)

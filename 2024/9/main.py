from typing import List

SAMPLE = False

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

cur_file_id = 0
last_file_id = n_files - 1
checksum = 0
i = 0
while cur_file_id <= last_file_id:
    cur_space = spaces[cur_file_id]
    print(i)

    # from left
    # print("left==")
    checksum += _checksum(i, i + files[cur_file_id] - 1, cur_file_id)
    i += files[cur_file_id]

    if cur_file_id == last_file_id:
        break

    # from right
    # print("right==")
    while cur_space > 0:
        # print("space:", cur_space)
        if files[last_file_id] >= cur_space:
            checksum += _checksum(i, i + cur_space - 1, last_file_id)
            i += cur_space
            files[last_file_id] -= cur_space
            cur_file_id += 1
            cur_space = 0
        else:
            checksum += _checksum(i, i + files[last_file_id] - 1, last_file_id)
            i += files[last_file_id]
            cur_space -= files[last_file_id]
            files[last_file_id] = 0
            last_file_id -= 1

print(debug_str)
print(checksum)

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


spaces.append(0)
n_files = len(files)
n_spaces = len(spaces)

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
cur = 0
for i in range(n_files):
    file = files[i]
    space = spaces[i]
    arr[cur : cur + file] = [i] * file
    cur += file
    arr[cur : cur + space] = [-1] * space
    cur += space

ans = 0
for i, v in enumerate(arr):
    if v == -1:
        continue
    ans += i * v
print(ans)

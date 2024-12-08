from itertools import product
from math import log10, pow

SAMPLE = False

filepath = "input/sample.in" if SAMPLE else "input/star.in"

data = {}
data_len = {}
with open(filepath) as f:
    for line in f.readlines():
        l, r = line.strip().split(":")
        r = r.strip().split(" ")
        data[int(l)] = list(map(int, r))
        data_len[int(l)] = list(map(lambda x: 10**len(x), r))
# print(data)

OPERATORS = [0, 1]
# 0: +
# 1: *

ans = set()
for k, v in data.items():
    n = len(v) - 1
    for comb in product(OPERATORS, repeat=n):
        x = v[0]
        for i, op in enumerate(comb):
            if op == 0:
                x += v[i + 1]
            elif op == 1:
                x *= v[i + 1]
        if k == x:
            ans.add(x)
print(sum(ans))

# part two

OPERATORS = [0, 1, 2]
# 2: concat

ans = set()
for k, v in data.items():
    n = len(v) - 1
    for comb in product(OPERATORS, repeat=n):
        x = v[0]
        for i, op in enumerate(comb):
            if op == 0:
                x += v[i + 1]
            elif op == 1:
                x *= v[i + 1]
            elif op == 2:
                # x = int(str(x) + str(v[i + 1]))
                x = x * data_len[k][i + 1] + data[k][i + 1]
        if k == x:
            ans.add(x)
print(sum(ans))

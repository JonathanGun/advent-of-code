from functools import lru_cache

SAMPLE = False
filename = "input/sample.in" if SAMPLE else "input/star.in"

nums = []
with open(filename) as f:
    nums = list(map(int, f.readline().strip().split()))
# print(nums)
# print(len(nums))


@lru_cache
def digits(num: int) -> int:
    if num < 0:
        return -1
    if num == 0:
        return 0
    return 1 + digits(num // 10)


def split(num: int, d: int):
    x = 10 ** (d // 2)
    l = num // x
    r = num % x
    return l, r


@lru_cache(maxsize=None)
def step(num: int, s: int):
    if s == 0:
        return 1
    if num == 0:
        return step(1, s - 1)

    d = digits(num)
    if d % 2 == 0:
        l, r = split(num, d)
        return step(l, s - 1) + step(r, s - 1)
    return step(num * 2024, s - 1)


print(sum(step(num, 25) for num in nums))
print(sum(step(num, 75) for num in nums))

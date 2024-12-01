def fn(ls: list[int]) -> list[int]:
    ret = [0] * (len(ls) - 1)
    for i in range(len(ret)):
        ret[i] = ls[i + 1] - ls[i]
    return ret

filename = "9.in"

ans1 = 0
ans2 = 0
with open(filename) as f:
    for line in f.readlines():
        cur1 = 0
        cur2 = 0
        sign = 1
        arr = list(map(int, line.split()))
        while any(arr):
            # print(arr)
            # print(arr[0] * sign, arr)
            cur1 += arr[-1]
            cur2 += arr[0] * sign
            sign *= -1
            arr = fn(arr)
        ans1 += cur1
        ans2 += cur2
        # print(cur1)
        # print(cur2)
print(ans1)
print(ans2)

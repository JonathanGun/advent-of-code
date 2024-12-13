import re
import numpy as np

SAMPLE = True

filename = "input/sample.in" if SAMPLE else "input/star.in"

prizes = []
buttons = []
regex_btn = r"Button .: X\+(\d+), Y\+(\d+)"
regex_prize = r"Prize: X=(\d+), Y=(\d+)"
with open(filename) as f:
    while True:
        btn_a = np.array(list(map(int, re.match(regex_btn, f.readline()).groups())))
        btn_b = np.array(list(map(int, re.match(regex_btn, f.readline()).groups())))
        buttons.append(np.array((btn_a, btn_b)))
        prizes.append(
            np.array(list(map(int, re.match(regex_prize, f.readline()).groups())))
        )
        if not f.readline():
            break
# print(prizes)
# print(buttons)

N = len(prizes)
W = np.array([3, 1])
ADDED = 10000000000000


def is_all_int(arr, EPS=1e-3):
    return np.all(abs(arr - np.round(arr)) < EPS)


# for i in range(N):
#     btn = buttons[i]
#     prize = prizes[i]
#     print(btn[0][0], btn[1][0], btn[0][1], btn[1][1], prize[0], prize[1])

ans1, ans2 = 0, 0
for i in range(N):
    eq_ans = np.linalg.solve(buttons[i].T, prizes[i])
    if is_all_int(eq_ans):
        ans1 += np.dot(W, eq_ans)
        print(i + 1, eq_ans, np.dot(W, eq_ans))
    eq_ans = np.linalg.solve(buttons[i].T, prizes[i] + ADDED)
    if is_all_int(eq_ans):
        ans2 += np.dot(W, eq_ans)
print(int(ans1))
print(int(ans2))

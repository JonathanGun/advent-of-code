from collections import defaultdict

limit = {
    'red': 12,
    'green': 13,
    'blue': 14,
}
ans = 0
with open("2.in") as f:
    for games in f:
        game_id_raw, game = games.split(":")
        _, game_id = game_id_raw.split(" ")
        pull = game.split(";")
        print(game_id)
        breaking = False
        pull_cnt = defaultdict(int)
        for balls in pull:
            print(balls)
            for ball in balls.split(","):
                cnt, color = ball.strip().split(" ")
                pull_cnt[color] = max(pull_cnt[color], int(cnt))

        # part 1
        #         if int(cnt) > limit[color]:
        #             if color not in limit.keys():
        #                 print("ASDASDAS")
        #                 breaking = True
        #             print(game_id, cnt, ">", limit[color], color)
        #             breaking = True
        #             break
        #     if breaking:
        #         break
        # if not breaking:
        #     ans += int(game_id)

        # part 2
        pull_power = 1
        for v in pull_cnt.values():
            pull_power *= v
        print(game_id, pull_cnt, pull_power)
        ans += pull_power
print(ans)

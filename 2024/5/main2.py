SAMPLE = False

rules_file = open("input/star.rules.in", "r")
if SAMPLE:
    rules_file = open("input/sample.rules.in", "r")

rules = []
with rules_file as f:
    for line in f:
        rules.append(list(map(int, line.split("|"))))

instructions = []
instructions_file = open("input/star.instructions.in", "r")
if SAMPLE:
    instructions_file = open("input/sample.instructions.in", "r")
with instructions_file as f:
    for line in f:
        instructions.append(list(map(int, line.strip().split(","))))

ans = 0
for instruction in instructions:
    valid = True
    for i, v in enumerate(instruction):
        for j, v2 in enumerate(instruction):
            if i >= j:
                continue
            if [v2, v] in rules:
                valid = False
                break
        if not valid:
            break
    if valid:
        ans += instruction[len(instruction) // 2]
print(ans)

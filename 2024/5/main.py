from collections import defaultdict

SAMPLE = False

rules_file = open("input/star.rules.in", "r")
if SAMPLE:
    rules_file = open("input/sample.rules.in", "r")

rules = defaultdict(set)
with rules_file as f:
    for line in f:
        (key, val) = line.split("|")
        l, r = int(key), int(val.strip())
        rules[l].add(r)
# for rule in sorted(rules):
#     print(rule, rules[rule], len(rules[rule]))
# print()

instructions = []
instructions_file = open("input/star.instructions.in", "r")
if SAMPLE:
    instructions_file = open("input/sample.instructions.in", "r")
with instructions_file as f:
    for line in f:
        instructions.append(list(map(int, line.strip().split(","))))

correct_ordered = [False for i in range(len(instructions))]
cnt = 0
for i, instruction in enumerate(instructions):
    head, *rest = instruction
    while rest:
        if set(rest) - rules[head]:
            break
        head, *rest = rest
    else:
        cnt += instruction[len(instruction) // 2]
        correct_ordered[i] = True
print(cnt)


def get_rank(items):
    filtered_rules = {key: rules[key] & items for key in items}
    return sorted(filtered_rules, key=lambda x: len(filtered_rules[x]))


# sort instructions
cnt2 = 0
for i, instruction in enumerate(instructions):
    if not correct_ordered[i]:
        sort_rules = get_rank(set(instruction))
        instruction.sort(key=lambda x: sort_rules.index(x))
        cnt2 += instruction[len(instruction) // 2]
        # print(instruction)
print(cnt2)

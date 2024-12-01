ans = 0
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
while line := input():
    cleaned = ""
    for i in range(len(line)):
        for j, word in enumerate(words):
            if line[i:].startswith(word):
                cleaned += str(j)
                break
        else:
            if '0' <= line[i] <= '9':
                cleaned += line[i]
    ans += int(cleaned[0] + cleaned[-1])
print(ans)

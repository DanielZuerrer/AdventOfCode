from collections import Counter

with open("input.txt") as file:
    lines = file.read().splitlines()

charCounts = list()
for i in range(len(lines[0])):
    chars = list()
    for line in lines:
        chars.append(line[i])
    charCounts.append(Counter(chars))

message = ''
for counts in charCounts:
    message += counts.most_common(1)[0][0]

print(message)
with open("input.txt") as file:
    rooms = file.read().splitlines()

letters = list()
ids = list()
checksums = list()

for room in rooms:
    words = room.split('-')
    letters.append("".join(words[0:-1]))
    ids.append(int(words[-1:][0].split('[')[0]))
    checksums.append(words[-1:][0].split('[')[1][:-1])


def getLetterFreqs(letters):
    freqs = dict()
    for char in letters:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
    return freqs


def getMostFrequent(freqs, amount):
    return [
        v[0] for v in sorted(
            freqs.items(), key=lambda kv: (-kv[1], kv[0]))
    ][0:amount]


mostFreq = list()
for room in letters:
    freqs = getLetterFreqs(room)
    mostFreq.append("".join(getMostFrequent(freqs, 5)))

idSum = 0
sensibleRooms = open("sensible.txt", 'w+')
for i in range(len(rooms)):
    if mostFreq[i] == checksums[i]:
        idSum += ids[i]
        sensibleRooms.write(rooms[i])
        sensibleRooms.write('\n')

sensibleRooms.close()
print(idSum)

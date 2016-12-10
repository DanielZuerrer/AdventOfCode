# read file into list of strings

with open("input.txt") as file:
    instructions = file.read().splitlines()

keypad = [[None, None, 1, None, None], [None, 2, 3, 4, None],
          [5, 6, 7, 8, 9], [None, 'A', 'B', 'C', None], [None, None, 'D', None, None]]
keyIndex = [2, 0]


def applyInstruction(instruction):
    global keyIndex

    for letter in instruction:

        prevIndex = [0, 0]
        prevIndex[0] = keyIndex[0]
        prevIndex[1] = keyIndex[1]

        if (letter == 'U'):
            keyIndex[0] = max(0, keyIndex[0] - 1)
        elif (letter == 'D'):
            keyIndex[0] = min(4, keyIndex[0] + 1)
        elif (letter == 'L'):
            keyIndex[1] = max(0, keyIndex[1] - 1)
        elif (letter == 'R'):
            keyIndex[1] = min(4, keyIndex[1] + 1)

        if keypad[keyIndex[0]][keyIndex[1]] is None:
            keyIndex = prevIndex

    return keypad[keyIndex[0]][keyIndex[1]]

for instruction in instructions:
    print(applyInstruction(instruction))

# read file into list of strings

with open("input.txt") as file:
    instructions = file.read().splitlines()

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
keyIndex = [1, 1]


def applyInstruction(instruction):
    for letter in instruction:
        if (letter == 'U'):
            keyIndex[0] = max(0, keyIndex[0] - 1)
        elif (letter == 'D'):
            keyIndex[0] = min(2, keyIndex[0] + 1)
        elif (letter == 'L'):
            keyIndex[1] = max(0, keyIndex[1] - 1)
        elif (letter == 'R'):
            keyIndex[1] = min(2, keyIndex[1] + 1)

    return keypad[keyIndex[0]][keyIndex[1]]

for instruction in instructions:
    print(applyInstruction(instruction))

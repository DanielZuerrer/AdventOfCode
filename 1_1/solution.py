directions = [
    "R3", "L5", "R2", "L1", "L2", "R5", "L2", "R2", "L2", "L2", "L1", "R2",
    "L2", "R4", "R4", "R1", "L2", "L3", "R3", "L1", "R2", "L2", "L4", "R4",
    "R5", "L3", "R3", "L3", "L3", "R4", "R5", "L3", "R3", "L5", "L1", "L2",
    "R2", "L1", "R3", "R1", "L1", "R187", "L1", "R2", "R47", "L5", "L1", "L2",
    "R4", "R3", "L3", "R3", "R4", "R1", "R3", "L1", "L4", "L1", "R2", "L1",
    "R4", "R5", "L1", "R77", "L5", "L4", "R3", "L2", "R4", "R5", "R5", "L2",
    "L2", "R2", "R5", "L2", "R194", "R5", "L2", "R4", "L5", "L4", "L2", "R5",
    "L3", "L2", "L5", "R5", "R2", "L3", "R3", "R1", "L4", "R2", "L1", "R5",
    "L1", "R5", "L1", "L1", "R3", "L1", "R5", "R2", "R5", "R5", "L4", "L5",
    "L5", "L5", "R3", "L2", "L5", "L4", "R3", "R1", "R1", "R4", "L2", "L4",
    "R5", "R5", "R4", "L2", "L2", "R5", "R5", "L5", "L2", "R4", "R4", "L4",
    "R1", "L3", "R1", "L1", "L1", "L1", "L4", "R5", "R4", "L4", "L4", "R5",
    "R3", "L2", "L2", "R3", "R1", "R4", "L3", "R1", "L4", "R3", "L3", "L2",
    "R2", "R2", "R2", "L1", "L4", "R3", "R2", "R2", "L3", "R2", "L3", "L2",
    "R4", "L2", "R3", "L4", "R5", "R4", "R1", "R5", "R3"
]

walkingDir = [0, 1, 0, -1, 0]
dirStart = 0
currentDir = walkingDir[dirStart:dirStart + 2]
position = [0, 0]


def updateCurrentDir(rotation):
    global dirStart

    if rotation == 'R':
        dirStart = (dirStart + 1) % 4
    elif rotation == 'L':
        dirStart = (dirStart - 1)
        if dirStart == -1:
            dirStart = 3

    return walkingDir[dirStart:dirStart + 2]


def updatePosition(direction):
    position[0] += direction[0]
    position[1] += direction[1]


for dir in directions:
    rotation = dir[0:1]
    currentDir = updateCurrentDir(rotation)
    walkX = currentDir[0] * int(dir[1:])
    walkY = currentDir[1] * int(dir[1:])
    position[0] += walkX
    position[1] += walkY

distanceFromStart = abs(position[0]) + abs(position[1])
print('Result: ' + str(position) + ' -> ' + str(distanceFromStart))

with open("input.txt") as file:
    textTriangles = file.read().splitlines()

stringTriangles = list()

for triangle in textTriangles:
    stringTriangles.append(triangle.split())

triangles = list()
for triangle in stringTriangles:
    triangles.append([int(x) for x in triangle])

columnTriangles = list()
index = 0
while index < len(triangles):
    columnTriangles.append([
        triangles[index][0], triangles[index + 1][0], triangles[index + 2][0]
    ])
    columnTriangles.append([
        triangles[index][1], triangles[index + 1][1], triangles[index + 2][1]
    ])
    columnTriangles.append([
        triangles[index][2], triangles[index + 1][2], triangles[index + 2][2]
    ])

    index += 3


def isTriangle(triangle):
    if (triangle[0] + triangle[1]) <= triangle[2]:
        return False
    elif (triangle[0] + triangle[2]) <= triangle[1]:
        return False
    elif (triangle[1] + triangle[2]) <= triangle[0]:
        return False

    return True


triangleCounter = 0
for triangle in columnTriangles:
    if isTriangle(triangle):
        triangleCounter += 1

print(triangleCounter)
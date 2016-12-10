with open("input.txt") as file:
    textTriangles = file.read().splitlines()

stringTriangles = list()

for triangle in textTriangles:
    stringTriangles.append(triangle.split())

triangles = list()
for triangle in stringTriangles:
    triangles.append([int(x) for x in triangle])


def isTriangle(triangle):
    if (triangle[0] + triangle[1]) <= triangle[2]:
        return False
    elif (triangle[0] + triangle[2]) <= triangle[1]:
        return False
    elif (triangle[1] + triangle[2]) <= triangle[0]:
        return False

    return True


triangleCounter = 0
for triangle in triangles:
    if isTriangle(triangle):
        triangleCounter += 1

print(triangleCounter)
import hashlib

inputText = 'cxdnnyjw'
pwd = ''


def getHash(integer):
    inputWithInt = inputText + str(integer)
    return hashlib.md5(bytes(inputWithInt, 'utf-8')).hexdigest()


integer = 0
while len(pwd) < 8:
    hashVal = getHash(integer)
    if hashVal[:5] == '00000':
        pwd += hashVal[5]
        print(pwd)
    integer += 1

print('Complete PWD: ' + pwd)

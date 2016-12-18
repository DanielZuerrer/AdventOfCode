import hashlib
from functools import reduce

inputText = 'cxdnnyjw'
pwd = [0] * 8
pwdSolved = 0


def getHash(integer):
    inputWithInt = inputText + str(integer)
    return hashlib.md5(bytes(inputWithInt, 'utf-8')).hexdigest()


integer = 0
while pwdSolved < 8:
    hashVal = getHash(integer)
    if hashVal[:5] == '00000':
        try:
            if pwd[int(hashVal[5])] == 0:
                pwd[int(hashVal[5])] = hashVal[6]
                print(pwd)
                pwdSolved += 1
        except:
            pass
    integer += 1

print('Complete PWD: ' + str(reduce(lambda x, y: x + y, pwd)))

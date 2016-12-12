with open("sensible.txt") as file:
    rooms = file.read().splitlines()

words = list()
ids = list()

for room in rooms:
    wordList = room.split('-')
    words.append(wordList[0:-1])
    ids.append(int(wordList[-1:][0].split('[')[0]))


def rotateChar(char, id):
    return chr((ord(char) - 97 + id) % 26 + 97)


decrypted = list()

for i in range(len(rooms)):
    decryptedWords = list()
    for word in words[i]:
        newWord = ""
        for char in word:
            newWord += rotateChar(char, ids[i])
        decryptedWords.append(newWord)
    decrypted.append(decryptedWords)

for i in range(len(decrypted)):
    if 'north' in decrypted[i] or 'pole' in decrypted[
            i] or 'northpole' in decrypted[i]:
        print(str(decrypted[i]) + " -> " + str(ids[i]))

if __name__ == '__main__':
    fileName = 'words.txt'
    with open(fileName, encoding='utf8') as file:
        count = {}
        for i, word in enumerate(file):
            lenKey = len(word.strip())
            count[lenKey] = count.get(lenKey, 0) + 1
    print(*count.items())

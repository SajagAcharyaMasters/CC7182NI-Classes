if __name__ == '__main__':
    fileName = 'Frankenstein.txt'
    with open(fileName, encoding='utf8') as file:
        lines = words = 0
        for line in file:
            lines += 1
            words += len(line.split())
    print(f'{fileName} has {lines} lines')
    print(f'{fileName} has {words} words')
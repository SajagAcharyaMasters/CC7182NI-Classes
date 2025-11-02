if __name__ == '__main__':
    fileName = 'words.txt'
    with open(fileName, encoding='utf8') as file:
        count5 = 0
        for i, line in enumerate(file):
            word = line.strip()
            count5 += len(word) == 5
    print(f'{count5} words have 5 letters only')

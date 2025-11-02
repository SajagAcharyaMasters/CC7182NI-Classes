if __name__ == '__main__':
    with open('testFile.txt', 'w') as file:
        file.write('hello\n')
        file.write('What\'s up guys')
    with open('testFile.txt') as file:
        print(file.read())
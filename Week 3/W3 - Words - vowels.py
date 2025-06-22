if __name__ == '__main__':
    fileName = 'words.txt'
    vowels = set('aeiou')
    with open(fileName, encoding='utf8') as file:
        count = 0
        for i, word in enumerate(file):
            count += len(vowels.intersection(word.lower())) == 5
    print(f'{count} words have all vowels')

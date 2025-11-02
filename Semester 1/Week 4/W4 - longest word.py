# input_word = 'typhoon'
input_word = input('Enter a word: ')
input_set = set(input_word.lower())
if __name__ == '__main__':
    fileName = '../Week 3/words.txt'
    with open(fileName, encoding='utf8') as file:
        matches = []
        for line in file:
            word = line.strip().lower()
            if set(word) == input_set:
                matches.append(word)
    matches = sorted(matches, key=len, reverse=True)
    print(*matches)
    print('Longest word:', matches[0] if len(matches) > 0 else None)
if __name__ == '__main__':
    fileName = 'words.txt'
    # Find 6-letter words and all their anagrams
    with open(fileName, encoding='utf8') as file:
        anagrams = {}
        for i, line in enumerate(file):
            word = line.strip()
            if len(word) == 6:
                # letters = list(word.lower())
                # letters.sort()
                # Below does the same as above
                letters = sorted(word.lower())
                letterKey = ''.join(letters)
                if letterKey not in anagrams:
                    anagrams[letterKey] = []
                anagrams[letterKey].append(word)
    for words in anagrams.values():
        if len(words) >= 6:
            print(words, sep='\n')


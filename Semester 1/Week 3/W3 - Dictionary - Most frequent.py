if __name__ == '__main__':
    fileName = 'Frankenstein.txt'
    wordCount = {}
    # Create dict of word count in file
    with open(fileName, encoding='utf8') as file:
        for line in file:
            words = line.split()
            for word in words:
                wordCount[word] = (wordCount[word] + 1) if word in wordCount else 1;
    # print(*wordCount.items())
    # Find the word with max frequency
    maxKey = max(wordCount, key=wordCount.get)
    print(f'"{maxKey}" occurred {wordCount[maxKey]} times in {fileName}')
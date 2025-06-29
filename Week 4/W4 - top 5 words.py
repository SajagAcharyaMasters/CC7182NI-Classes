if __name__ == '__main__':
    fileName = '../Week 3/Frankenstein.txt'
    wordCount = {}
    # Create dict of word count in file
    with open(fileName, encoding='utf8') as file:
        for line in file:
            words = line.split()
            for word in words:
                wordCount[word] = (wordCount[word] + 1) if word in wordCount else 1;
    # print(*wordCount.items())
    # Find top 5 words
    top5 = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)[:5]
    print(sorted(wordCount, key=lambda k: wordCount[k], reverse=True)[:5])
    for i, (word, count) in enumerate(top5):
        print(f'{i}. {word}\t: {count}')


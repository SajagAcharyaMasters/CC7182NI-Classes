if __name__ == '__main__':
    fileName = 'words.txt'
    anagrams = {}
    n = 6
    with open(fileName) as fp:
        for line in fp:
            word = line.strip()
            if n == len(word):
                key = tuple(sorted(word))
                anagrams[key] = anagrams.get(key,[]) + [word]
    for group in anagrams.values():
        if len(group) >= n:
            print(group)


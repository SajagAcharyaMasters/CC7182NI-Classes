# with open('myfile', 'w') as fp:
#     fp.write('hello\n')
#     fp.write('this file is written from python')
# with open('myfile') as fp:
#     data = fp.read()
#     print(data)
# with open('practice.py') as fp:
#     for line in fp:
#         print(end=line)

#FRANKENSTEIN
# file =  'Frankenstein.txt' 
# count = 0
# with open (file, encoding='utf8') as fp:
#     for i, line in enumerate(fp):
#         count +=  len(line.split())
# print(file, 'has', i, 'lines')
# print(file, 'has', count, 'words')

#WORDS
# file = 'words.txt'
# count_in = count_starts = 0
# with open ('words.txt') as fp:
#     for line in fp:
#         count_in += ('program' in line)
#         count_starts += line.startswith('program')
# print(count_in,'words has "program"')
# print(count_starts, 'words start with "program"')

#COUNT 5 LETTER WORDS
# file = 'words.txt'
# count = 0
# with open(file, encoding='utf8') as fp:
#     for line in fp:
#         words = line.split()
#         for word in words:
#             cleaned = word.strip()
#             if len(cleaned) == 5:
#                 count += 1
# print(count)

#COUNT WORDS WITH ALL VOWELS
# file = 'words.txt'
# vowel =  set('aeiou')
# count = 0
# with open(file, encoding='utf8') as fp:
#     for line in fp:
#         words = line.split()
#         for word in words:
#             letters = set(word.lower())
#             if vowel.issubset(letters):
#                 count += 1
# print(count)

#DICTIONARY
# print(type({}))
# print(type(dict()))
# print({
#     100: 'integer',
#     1.0: 'float',
#     1.5: 'float',
#     1j: 'complex',
#     (1,2): 'pair tuple',
#     True: 'bool-true',
#     False : 'bool-false',
#     bool : 'ok this is going insane',
#     int: 'or its just a trailer'
# })

#COUNT LETTER FREQUENCY
# freq = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
# for c in input('phrase:'):

#COUNT CHAR FREQUENCY
# phrase = 'list of punctuations are ,.!;'
# print(f'{phrase=}')
# freq = {}
# for c in phrase:
#     freq[c] = (freq[c]+1) if (c in freq) else 1
# print(*freq.keys())
# print(*freq.values())

#WORD LENGTH DISTRIBUTION
# freq = {}
# with open('words.txt', encoding='utf8') as fp:
#     for line in fp.readlines():
#         l = len (line.strip())
#         freq[l] = freq.get(l,0) + 1
# print('word length distribution of words file')
# print(sorted(freq.items()))

#MOST FREQUENT WORDS
# freq = {}

# with open('words.txt', encoding='utf8') as fp:
#     for line in fp:
#         for word in line.split():
#             clean = ''.join(c for c in word if c.isalpha()).lower()
#             if clean:
#                 freq[clean] = freq.get(clean, 0) + 1

# most_frequent = max(freq.items(), key=lambda x: x[1])
# print(f'{most_frequent[0]}:{most_frequent[1]} times')

#NUMBER TO WORDS

# SIR SKIPPED THIS


#NUMBER PLACE10

# SKIPPED THIS AS WELL


#CONCATENATION
# print([1, 2, 3] + [4, 5, 6])
# print((1, 2, 3) + (4, 5, 6))
# print('abc' + 'efg')

#REPEAT
# print((0, 1) * 5)
# print((1, 2) * 5)
# print('abc ' * 5)

#SEARCH
# a = [10, 20, 30]
# print(i:=a.index(20), a[i])
# t = (40, 50, 60)
# print(i:=t.index(60), t[i])
# s = 'hello world'
# print(i:=s.index('world'), s[i:])

#6 LETTER WORD 6 ANAGRAMS
# anagrams = {}
# n=6
# with open('words.txt') as fp:
#     for line in fp:
#         word = line.strip()
#         if n != len(word): continuekey = tuple(sorted(word))
#         key = tuple(sorted(word))
#         anagrams[key]=anagrams.get(key,[])+[word]
# for group in anagrams.values():
#     if len(group) >= n:
#         print(group)

#COPY
# a = list(range(10))
# b = a
# b[0] = 100
# print(a)
# print(b)
# print(id(a), id(b))

#ITERATIONS
# it = iter('py')
# print(it)
# print(type(it))
# print(next(it))
# print(next(it))
# try:
#     next(it)
# except StopIteration as e:
#     print('oops!')

#UNDUMPIFY
# d = iter('67726561742c20796f752063616e207265616421')
# for i,j in zip(d, d):
#     print(chr(int(i+j, 16)), end = '')

#ZIP
# print(*enumerate('hello'))
# print(*zip(range(5), 'hello'))
# print(*zip(range(3), 'hello'))

# print(dict(zip([5, 6], ['five', 'six'])))
# print(dict(enumerate('SMTWTFS', 1)))

#GENERATOR
# def gen():
#     yield 1
#     yield 2
#     yield 'done'
# g = gen()
# print(g, type(g))
# print(next(g))
# print(*g)
# for i in gen():
#     print(i)

#FIBONACCI GENERATOR
# def fib_gen():
#     a, b = 0, 1
#     while True: 
#         yield a
#         a, b = b, a + b
# fib = fib_gen()
# print(next(fib))
# print(next(fib))

#UNPACK
# cpu, ram, (hdd, ssd) = 'Ryzen 7535U', [8, 8], (256, 512)
# print(cpu, ram, hdd, ssd, sep='\n')

# a, b, c = '123'
# print(a, b, c)

# for i, c in enumerate('hi'):
#     print(i, c)

#GLOBBING
# *x, y, z = range(10); print(x, y, z)
# x, *y, z = range(10); print(x, y, z)
# x, y, *z = range(10); print(x, y, z)

# x, y, *z = (0, 1)
# print(x, y, z)
# x, y, *z = range(5)
# print(x, y, z)

#SPREAD
# print([1, 2, *[4, *[5, 6]]])
# print(*[1, 2, *[4, *[5, 6]]])

# a = [ 1, 2, 3 ]
# b = [ 4, 5, 6 ]
# x = [ a, b ]
# print(x)
# y = [ *a, *b ] 
# print(y)
# b.extend(a)
# print(b)

#DICT
# x = {1:'a', 2:'b'}
# y = x
# y[1] = 'changed'
# print(x)
# print(y)
# print(id(x), id(y))

# x = {1:'a', 2:'b'}
# y = {3:'c', 4:'d'}
# z = x.copy()
# z.update(y)
# print(id(x), id(y), id(z))
# print({**x, **y})

#IS AND EQUALS
# a = list()
# b = a
# c = a.copy()
# print(a is b)
# print(a == b)
# print(a is c)
# print(a == c)

#FUNCTION PARAMS
def foo(*args, **kwargs):
    print(args, kwargs)
    print()
foo(1, 2, 3)
foo(a=1, b=2, c=3)
a, d = [0, 1], {'a':3, 'b':4}
foo(a, d)
foo(*a, **d)
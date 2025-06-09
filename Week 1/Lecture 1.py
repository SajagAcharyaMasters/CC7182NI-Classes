

def charInfo():
    inp = input('Enter a character: ')
    ascii = ord(inp)
    print('dec:', ascii)
    print('bin:', bin(ascii), format(ascii, 'b'))
    print('hex:', hex(ascii), format(ascii, 'x'))


if __name__ == '__main__':
    charInfo()
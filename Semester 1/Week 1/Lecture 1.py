

def charInfo():
    inp = input('Enter a character: ')
    ascii = ord(inp)
    print('dec:', ascii)
    print('bin:', bin(ascii), format(ascii, 'b'))
    print('hex:', hex(ascii), format(ascii, 'x'))

def whileLooper():
    acc = inp = 0
    count = 0
    minm = maxm = None # Using list, min(list) and max(list) works
    while inp != 'q':
        inp = input('Enter number (q to quit): ')
        try:
            x = int(inp)
            acc += x
            count += 1
            if  minm is None or x < minm: minm = x
            elif maxm is None or x > maxm: maxm = x
            print('sum:', acc)
        except Exception as e:
            # continue
            print(f'Invalid input: {inp}' if inp != 'q' else f'\nFinal sum: {acc}')
    print('Average:', acc / count)
    print('Min:', minm)
    print('Max:', maxm)

if __name__ == '__main__':
    whileLooper()
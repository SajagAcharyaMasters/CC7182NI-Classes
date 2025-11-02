if __name__ == '__main__':
    with open('Lab 2 - Read self.py') as file:
        i = 0
        for line in file:
            i += 1
            print(f'{i:02}', line, end='') # new line issue fix
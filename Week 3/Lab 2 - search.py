if __name__ == '__main__':
    fileName = 'words.txt'
    with open(fileName, encoding='utf8') as file:
        has = contains = 0
        search = 'program'
        for i, line in enumerate(file):
            has += search in line
            contains += line.startswith(search)
    print(f'{has} words have "{search}"')
    print(f'{contains} words start with "{search}"')

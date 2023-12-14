def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if '\n' in lines[i]:  # remove newline characters
            lines[i] = lines[i][:len(lines[i]) - 1]

    platform = {}
    platform['h'] = len(lines)
    platform['w'] = len(lines[0])
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '.':
                platform[(i, j)] = 0
            if lines[i][j] == 'O':
                platform[(i, j)] = 1
            if lines[i][j] == '#':
                platform[(i, j)] = 2

    tilt_platform(platform)
    # visualize_platform(platform)
    print('Total load: {}'.format(calculate_load(platform)))


def calculate_load(platform):
    load = 0
    for i in range(platform['h']):
        row_value = platform['h'] - i
        for j in range(platform['w']):
            if platform[(i, j)] == 1:
                load += row_value
    return load


def tilt_platform(platform):
    for n in range(platform['h']-1):
        for i in range(1, platform['h']):
            for j in range(platform['w']):
                if (platform[(i, j)] == 1) and (platform[(i-1, j)]) == 0:
                    platform[(i-1, j)] = 1
                    platform[(i, j)] = 0


def visualize_platform(platform):
    for i in range(platform['h']):
        for j in range(platform['w']):
            char = '.' if platform[(i, j)] == 0 else 'O' if platform[(i, j)] == 1 else '#'
            print(char, end='')
        print()


if __name__ == '__main__':
    main()
def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    platform = {'h': len(lines), 'w': len(lines[0])}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '.':
                platform[(i, j)] = 0
            if lines[i][j] == 'O':
                platform[(i, j)] = 1
            if lines[i][j] == '#':
                platform[(i, j)] = 2

    loads = {}  # load calculated containing array of cycles
    for i in range(100):
        spin_cycle(platform)
        load = calculate_load(platform)
        if load not in loads:
            loads[load] = []
        loads[load].append(i)
        print('cycles {:3} | load {:6}'.format(i+1, load))

    print('Total load: {}'.format(load))


def calculate_load(platform):
    load = 0
    for i in range(platform['h']):
        row_value = platform['h'] - i
        for j in range(platform['w']):
            if platform[(i, j)] == 1:
                load += row_value
    return load


def spin_cycle(platform):
    # tilt up
    for n in range(platform['h'] - 1):
        for i in range(1, platform['h']):
            for j in range(platform['w']):
                if (platform[(i, j)] == 1) and (platform[(i - 1, j)]) == 0:
                    platform[(i - 1, j)] = 1
                    platform[(i, j)] = 0
    # tilt left
    for n in range(platform['w'] - 1):
        for i in range(platform['h']):
            for j in range(1, platform['w']):
                if (platform[(i, j)] == 1) and (platform[(i, j - 1)]) == 0:
                    platform[(i, j - 1)] = 1
                    platform[(i, j)] = 0
    # tilt down
    for n in range(platform['h'] - 1):
        for i in range(platform['h'] - 1):
            for j in range(platform['w']):
                if (platform[(i, j)] == 1) and (platform[(i + 1, j)]) == 0:
                    platform[(i + 1, j)] = 1
                    platform[(i, j)] = 0
    # tilt right
    for n in range(platform['w'] - 1):
        for i in range(platform['h']):
            for j in range(platform['w'] - 1):
                if (platform[(i, j)] == 1) and (platform[(i, j + 1)]) == 0:
                    platform[(i, j + 1)] = 1
                    platform[(i, j)] = 0


def visualize_platform(platform):
    for i in range(platform['h']):
        for j in range(platform['w']):
            char = '.' if platform[(i, j)] == 0 else 'O' if platform[(i, j)] == 1 else '#'
            print(char, end='')
        print()


if __name__ == '__main__':
    main()

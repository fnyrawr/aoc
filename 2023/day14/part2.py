def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    height = len(lines)
    width = len(lines[0])
    platform = {(i, j): 0 if lines[i][j] == '.' else 1 if lines[i][j] == 'O' else 2 for i in range(height) for j in range(width)}
    init_platform = platform

    formations = {}
    total = 1000000000
    num_to_run = 0

    for i in range(total):
        platform = spin_cycle(platform, height, width)
        formation = str(platform)
        if formation not in formations:
            formations[formation] = i
        else:
            period = i - formations[formation]
            num_to_run = (total - (i+1)) % period
            formations[formation] = i
            break

    for _ in range(num_to_run):
        platform = spin_cycle(init_platform, height, width)

    print('Total load: {}'.format(calculate_load(platform, height, width)))


def calculate_load(platform, height, width):
    load = 0
    for i in range(height):
        row_value = height - i
        for j in range(width):
            if platform[(i, j)] == 1:
                load += row_value
    return load


def spin_cycle(platform, height, width):
    # tilt up
    for n in range(height - 1):
        for i in range(1, height):
            for j in range(width):
                if (platform[(i, j)] == 1) and (platform[(i - 1, j)]) == 0:
                    platform[(i - 1, j)] = 1
                    platform[(i, j)] = 0
    # tilt left
    for n in range(width - 1):
        for i in range(height):
            for j in range(1, width):
                if (platform[(i, j)] == 1) and (platform[(i, j - 1)]) == 0:
                    platform[(i, j - 1)] = 1
                    platform[(i, j)] = 0
    # tilt down
    for n in range(height - 1):
        for i in range(height - 1):
            for j in range(width):
                if (platform[(i, j)] == 1) and (platform[(i + 1, j)]) == 0:
                    platform[(i + 1, j)] = 1
                    platform[(i, j)] = 0
    # tilt right
    for n in range(width - 1):
        for i in range(height):
            for j in range(width - 1):
                if (platform[(i, j)] == 1) and (platform[(i, j + 1)]) == 0:
                    platform[(i, j + 1)] = 1
                    platform[(i, j)] = 0
    return platform


def visualize_platform(platform, height, width):
    for i in range(height):
        for j in range(width):
            char = '.' if platform[(i, j)] == 0 else 'O' if platform[(i, j)] == 1 else '#'
            print(char, end='')
        print()


if __name__ == '__main__':
    main()

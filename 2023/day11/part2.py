def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    # get lines without galaxy
    galaxies = []
    for i in range(len(lines)):
        if '\n' in lines[i]:  # remove newline characters
            lines[i] = lines[i][:len(lines[i]) - 1]

    void_rows = []
    void_cols = []
    # get rows without galaxy
    for i in range(len(lines)):
        if not '#' in lines[i]:
            void_rows.append(i)
    # get columns without galaxy
    for j in range(len(lines[0])):
        galaxy_found = False
        for i in range(len(lines)):
            if lines[i][j] == '#':
                galaxy_found = True
        if not galaxy_found:
            void_cols.append(j)

    # get galaxies and expand them according to voids
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                galaxies.append([i, j])
    for k in range(len(galaxies)):
        offset_rows = 0
        for i in void_rows:
            if galaxies[k][0] > i:
                offset_rows += 999999
        galaxies[k][0] += offset_rows
        offset_cols = 0
        for j in void_cols:
            if galaxies[k][1] > j:
                offset_cols += 999999
        galaxies[k][1] += offset_cols

    # calculate distances between pairs
    sum_distances = 0
    for k in range(len(galaxies) + 1):
        for n in range(k + 1, len(galaxies)):
            distance = calculate_distance(galaxies[k], galaxies[n])
            sum_distances += distance
    print('distances total: {}'.format(sum_distances))


def calculate_distance(a, b):
    return abs((a[0]) - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    main()

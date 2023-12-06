def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    # parse times
    times = lines[0].split(':')[1].strip().split(' ')
    while '' in times:
        times.remove('')
    times = list(map(int, times))
    # parse distances
    distances = lines[1].split(':')[1].strip().split(' ')
    while '' in distances:
        distances.remove('')
    distances = list(map(int, distances))
    print('Times: {}'.format(times))
    print('Distances: {}'.format(distances))

    # for each race
    total_combinations = 1
    for i in range(0, len(times)):
        combinations = 0
        for k in range(0, times[i]):
            if (times[i] - k)*k > distances[i]:
                combinations += 1
        total_combinations *= combinations

    print('Combinations total: {}'.format(total_combinations))


if __name__ == '__main__':
    main()
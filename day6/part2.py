def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    # parse time
    time = ''
    for c in lines[0].split(':')[1].strip():
        if c != ' ':
            time += c
    time = int(time)
    # parse distance
    distance = ''
    for c in lines[1].split(':')[1].strip():
        if c != ' ':
            distance += c
    distance = int(distance)
    print('Time: {}'.format(time))
    print('Distance: {}'.format(distance))

    # get combinations
    combinations = 0
    for k in range(0, time):
        if (time - k) * k > distance:
            combinations += 1

    print('Combinations total: {}'.format(combinations))


if __name__ == '__main__':
    main()
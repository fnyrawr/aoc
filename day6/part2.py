from math import floor, ceil, sqrt


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
    b1 = floor((time + sqrt(time * time - 4 * (distance + 1))) / 2)
    b2 = ceil((time - sqrt(time * time - 4 * (distance + 1))) / 2)
    combinations = (b1 - b2 + 1)

    print('Combinations total: {}'.format(combinations))


if __name__ == '__main__':
    main()